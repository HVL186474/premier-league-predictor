# Report notes

Facts, numbers and findings to use in the individual reports. These are notes, not report text: each of us writes our own report in our own words. Add to this file whenever something is decided or measured, with the date.

All log loss numbers are on the **2024/25 validation season** unless they say otherwise. Lower is better.

## 1. Data

- Source: football-data.co.uk, `E0.csv` per season, 2016/17 to 2026/27. 3,850 matches loaded on 2026-10-21 (10 full seasons of 380, plus 50 matches of 2026/27).
- Split by season (`src/split.py`, decision D4): 2016/17 warm-up only, train 2017/18 to 2023/24 (2,660 matches), validation 2024/25 (380), test 2025/26 (380). 2026/27 is not in any set; the app uses it for current ratings.
- Splits are by season, never random, so the model never trains on matches played after the ones it is scored on.
- **Date pitfall** (decision D6): the 2016/17 file writes dates as `13/08/16`, later seasons as `11/08/2017`. Dates must be parsed with `dayfirst=True, format="mixed"`, or the order of matches can come out wrong, and Elo and form are then built from the wrong history.
- Results in 2024/25: home win 40.8%, away win 34.7%, draw 24.5%.

## 2. Leakage rules and how we test them

- A feature is allowed only if it is known before kick-off. Match statistics (goals, shots, cards) and closing odds are forbidden as features (blueprint §2).
- Betting odds are a **benchmark only**, never a model input (decision D1), so the model is our own work.
- Form uses `shift(1)` before the rolling mean, so a match never sees its own result.
- Elo stores each team's rating **before** the match, then updates it.
- Tests (`tests/test_features.py`): changing a match's result must not change that match's own features, only later ones. Same check for form and for Elo.
- Missing form (a team's first match) is filled with 0.79 (decision D3). *TODO: explain where 0.79 comes from.*

## 3. Elo

- Start at 1500. Promoted teams start at the average rating of the teams that were relegated, so the league total stays the same.
- K = 30 (changed from 20 on 2026-10-21, see §5). K is how many points a result can move a rating.
- Example with K = 20: two 1500 teams, home team wins. Expected score 0.5, actual 1, so the home team gains 20 × 0.5 = 10 and the away team loses 10.
- One team's gain is always the other's loss (tested: ratings sum is conserved).
- **Bug found and fixed (2026-10-21):** the first version collected ratings in a list in sorted order, then attached the list to the unsorted frame by position. Matches on the same date could get each other's ratings. Fixed by storing each rating under the row's index label and using a stable sort. A test shuffles the input to prove it.

## 4. Evaluation

- Main metric: **log loss**. For each match, take the probability the model gave to what actually happened and penalise it when it's low (−ln p). Average over all matches.
  - 60% on the actual result costs 0.51, 33% costs 1.10, 10% costs 2.30. Being confidently wrong costs a lot.
  - Guessing a third each for every match gives ln 3 = 1.099.
- Why not accuracy: accuracy only counts the single most likely result, so it can't reward good probabilities. A gap of 0.01 in accuracy is about 4 matches out of 380.
- Model choice rule (decision D5, agreed 2026-10-21 **before** seeing any results): a gap under 0.005 log loss is a tie, and the simpler model (logistic regression) wins a tie.
- Test season 2025/26 is used **once**, for the final number (T3.5).

## 5. Results so far

### Validation, K = 20 (T3.2, 2026-10-21)

| Model | Log loss | Accuracy |
|---|---|---|
| Bet365 implied probabilities (benchmark) | 0.9708 | 54.2% |
| Logistic regression: Elo only | 0.9819 | 53.2% |
| Logistic regression: Elo + form | 0.9820 | 53.4% |
| Logistic regression: form only | 1.0429 | 49.2% |
| Class frequencies from training | 1.0809 | 40.8% |

### Validation, K = 30 (after T3.3, 2026-10-21)

| Model | Log loss | Accuracy |
|---|---|---|
| Bet365 (benchmark) | 0.9708 | 54.2% |
| Logistic regression: Elo + form | 0.9763 | 54.0% |
| Logistic regression: Elo only | 0.9774 | 53.7% |
| Logistic regression: form only | 1.0429 | 49.2% |
| Class frequencies | 1.0809 | 40.8% |

Elo + form vs Elo only is a 0.0011 gap, a tie under D5.

### Feature experiments (T3.3, 2026-10-21)

Logistic regression on validation, compared with Elo only at K = 20 (0.9819):

| Candidate | Best result | Change | Verdict |
|---|---|---|---|
| Form, last 5 matches | 0.9820 | +0.0001 | No help |
| Goal-difference form, last 5 / 10 / 19 / 38 matches | 0.9814 (38) | −0.0005 | No help |
| Home bonus inside Elo, 50 / 70 / 100 points | 0.9821 (50) | +0.0002 | No help: the model's intercept already learns home advantage |
| Elo weighted by goal margin | 0.9836 (K = 30) | +0.0017 | Worse |
| Pull ratings toward the average between seasons, 20 / 33 / 50% | 0.9782 (33%) | −0.0037 | Small gain alone, nothing extra once K is higher |
| **Higher K: 25 / 30 / 35** | **0.9773 to 0.9787** | **−0.0046** | **Only real gain.** Every value from 25 to 35 beats 20, so it's a stable effect, not one lucky number |

We looked at validation 15+ times to choose K, so the validation score is a little flattering. That is why the test set is kept for one final run.

### Gradient boosting (T3.4, 2026-10-23)

`HistGradientBoostingClassifier(max_depth=2, learning_rate=0.05, max_iter=100)`, K = 30, same split and rows. Run once with these settings, not tuned on validation.

| Model | Log loss | Accuracy |
|---|---|---|
| Bet365 (benchmark) | 0.9708 | 54.2% |
| Logistic regression: Elo + form | 0.9763 | 54.0% |
| Logistic regression: Elo only | 0.9774 | 53.7% |
| Boosting: Elo only | 0.9926 | 54.0% |
| Boosting: Elo + form | 0.9956 | 53.4% |
| Boosting: form only | 1.0493 | 50.0% |

Boosting is 0.015 worse than logistic regression on the same features, three times the D5 tie threshold. The Elo effect is smooth, so the trees' extra flexibility only fits noise in 2,660 training matches.

### Model choice (D5, 2026-10-23)

- Boosting loses outright to logistic regression.
- Logistic regression Elo + form vs Elo only: gap 0.0011, a tie under D5, so the simpler model wins.
- **Chosen model: logistic regression on `EloDiff` only, K = 30.**

### Scoring check

- `score()` (T2.7, 2026-10-23): logistic regression on `EloDiff` with K = 20, trained on the training seasons and scored on 2025/26, gives 1.0417 log loss and 47.6% accuracy, matching blueprint §3.
- Note for honesty: while setting up this check, the same model was also scored on 2025/26 at K = 30 (1.039). That number was not used for any decision; the choice above was made on validation only.

### Test season 2025/26 (T3.5, 2026-10-23, `src/final_evaluation.py`)

Every model trained on train + validation (2017/18 to 2024/25), the seasons played before the test season. So these numbers differ slightly from the blueprint §3 table, which trained on train only.

| Model | Log loss | Accuracy |
|---|---|---|
| Class frequencies | 1.0850 | 42.6% |
| Logistic regression: Elo only, K = 20 (baseline) | 1.0405 | 47.4% |
| **Logistic regression: Elo only, K = 30 (chosen)** | **1.0385** | **48.7%** |
| Bet365 (benchmark) | 1.0185 | 49.0% |

- Success criterion (blueprint §3) met: the chosen model beats the Elo-only baseline on validation and on test.
- But the K = 30 gain shrank from 0.0046 (validation) to 0.0020 (test). Expected, since K was picked after looking at validation 15+ times.
- Closes 70% of the gap from knowing nothing to the bookmaker on test (94% on validation). Gap to Bet365: 0.020 on test vs 0.007 on validation.
- Draws were 27.4% of test matches (104 of 380). Neither the model nor Bet365 predicts a single draw.
- Figures: `figures/confusion_matrix.png`, `figures/calibration.png`.
  - Calibration: home and away follow the diagonal well up to about 50%. At the top the model is a bit overconfident (says 73% home win, happened 62%).
  - Draw probabilities stay between 17% and 26%, and within that band they are roughly right.
- Process: the script was not committed before running. It ran twice: the first run crashed on a missing import after printing the table; the model is deterministic, so the numbers were the same.

## 6. Findings to discuss

- **Elo does most of the work.** From knowing nothing (1.081) to the bookmaker (0.971) is a gap of 0.110. Elo-only logistic regression closes 90% of it at K = 20, and 94% at K = 30.
- **Form adds almost nothing on top of Elo.** A team in good form is winning, so its Elo is already rising. Elo also accounts for who you beat and remembers more than 5 matches. Goal difference didn't help either.
- **K = 20 reacts too slowly.** A higher K lets ratings follow how strong teams are now.
- **The remaining gap to the bookmaker** (0.006 at K = 30) is mostly information we don't use and is out of scope: injuries, line-ups, transfers.
- **No model ever predicts a draw, not even the bookmaker.** Draws were 24.5% of matches. The model gives draws 22% on average (Bet365: 23%), so its draw probabilities are realistic. But its highest draw probability for any single match is 25% (Bet365: 31%), so a home or away win is always more likely. This is how football works, not a bug, and it's a reason to score probabilities with log loss and not picks with accuracy.
- **2024/25 was an unusually predictable season:** all three promoted teams (Ipswich, Leicester, Southampton) went straight back down. Validation scores (about 0.98) are much better than the Elo baseline on the 2025/26 test season (1.042). Only compare models on the same season, never validation numbers with test numbers.

## 7. Process

- Spec-first: the blueprint (`docs/BLUEPRINT.md`) and task list (`docs/task.md`) were written before the code, and decisions D1 to D6 are recorded there with dates.
- Tests: 28 pytest tests on 2026-10-21, covering form, Elo, the split and the comparison code.
- Work split: Alexander did features, the split and the model comparison. Andreas did data loading, preprocessing, evaluation and the app.
- 2026-10-21: Andreas's branch was built on an old commit and conflicted with `main` in 5 files. Merged together, keeping his preprocessing and Alexander's features.
