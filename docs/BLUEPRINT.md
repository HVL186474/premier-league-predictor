# Blueprint: Premier League Predictor

DAT158 ML assignment 2. This document is the agreed spec. Code changes should trace back to it and to a task in [task.md](task.md). If something here needs to change, change it here first.

## 1. Goal

Predict the result of a Premier League match **before it is played**, as probabilities for:

- **H**: home win
- **D**: draw
- **A**: away win

Show those probabilities in a Streamlit app for any fixture between two teams in the current season.

## 2. Data

| Item | Decision |
|---|---|
| Source | [football-data.co.uk](https://www.football-data.co.uk/englandm.php), file `E0.csv` per season |
| Seasons | 2016/17 to 2026/27 (11 seasons, ~3,850 matches) |
| Loader | `src/data_loader.py`: `download_seasons()` then `load_matches()` |
| Target column | `FTR` (full-time result: `H` / `D` / `A`) |
| Dates | Text, day first. 2016/17 uses 2-digit years (`13/08/16`), later seasons 4-digit (`11/08/2017`). `preprocessing.py` parses them with `pd.to_datetime(..., dayfirst=True, format="mixed")` so every season has real dates (decision D6) |
| Current season | 2026/27 is still being played. Re-download it to get new results |

### Allowed and forbidden inputs

A feature is allowed only if it is known **before kick-off**.

- **Allowed**: date, home team, away team, anything computed from **earlier** matches (form, Elo, goal difference so far).
- **Benchmark only, never a feature**: pre-match betting odds such as `B365H`/`B365D`/`B365A` (decision D1).
- **Forbidden as features** (they describe the match itself, so they leak the result): `FTHG`, `FTAG`, `FTR`, `HTHG`, `HTAG`, `HTR`, `HS`, `AS`, `HST`, `AST`, `HF`, `AF`, `HC`, `AC`, `HY`, `AY`, `HR`, `AR`, and closing odds (bookmaker prefix followed by `C`, e.g. `B365CH`, `PSCD`, `AvgCA`, `MaxC>2.5`). Closing odds are set just before kick-off, so they aren't available when the app predicts days ahead.

Every rolling or rating feature must use `shift(1)`, or be computed from the state before the match, so a match never sees its own result.

## 3. Evaluation

| Item | Decision |
|---|---|
| Warm-up season | 2016/17 is used to build up Elo ratings and form, but **not for training**, because every team starts at 1500 with no history (decision D4) |
| Training data | Seasons 2017/18 to 2023/24 |
| Validation data | 2024/25, used for choosing features and tuning |
| Test data | 2025/26 (380 matches), used **once** for the final numbers in the report |
| Final model | Retrained on 2017/18 to 2025/26 before going into the app |
| Primary metric | **Log loss**. We output probabilities, so we score probabilities |
| Secondary metrics | Accuracy, confusion matrix, share of draws predicted |

Splits are by season, never random, so the model never trains on matches after the ones it is tested on.

### Scoring

Every model is scored with the same function, `score(model, X, y)` in `src/evaluation.py`:

- It takes a fitted sklearn model, the feature columns `X` and the true results `y` (`FTR`).
- It returns a dict: `{"log_loss": ..., "accuracy": ...}`.
- Log loss uses `model.predict_proba(X)` with `labels=model.classes_`, so the class order is always right.
- **Check**: logistic regression on `EloDiff` only, trained on the training seasons and scored on 2025/26, must give **1.042** (re-measured 2026-10-21 with `src/split.py`; the 1.043 in the table below came from the notebook). If it doesn't, the function is wrong.

### Baselines to beat (2025/26, measured 2026-10-16)

| Model | Accuracy | Log loss |
|---|---|---|
| Class frequencies / always predict H | 42.6% | 1.085 |
| Logistic regression on form only (notebook) | 43.4% | n/a |
| Logistic regression on Elo difference only | 47.6% | 1.043 |
| Bet365 implied probabilities (reference ceiling) | 48.9% | 1.019 |

**Success criterion**: beat the Elo-only model on log loss in validation and test, and report how close we get to the bookmaker.

## 4. Features (initial set)

| Feature | Definition |
|---|---|
| `HomeElo`, `AwayElo`, `EloDiff` | Elo ratings before the match. Start at 1500, K = 20. Promoted teams start at the average of the relegated teams |
| `HomeForm`, `AwayForm` | Average points from the team's previous 5 league matches |
| Candidates to test | Separate home/away form, goal-difference form, Elo home advantage, pulling ratings toward average between seasons |

Missing form (a team's first match in the data) is filled with **0.79** (decision D3). The report should say where this number comes from.

## 5. Models

1. Multinomial logistic regression: the main, explainable model.
2. A gradient-boosted tree model (e.g. `HistGradientBoostingClassifier`) for comparison.
3. Pick the one with the lower validation log loss. If the gap is under **0.005**, it counts as a tie and logistic regression wins (decision D5).

Draws are hard to predict, and no model is expected to *pick* draws often. The report should discuss this.

## 6. Code structure

| Module | Responsibility |
|---|---|
| `src/data_loader.py` | Download and load raw seasons (paths relative to the project root) |
| `src/preprocessing.py` | Parse dates, sort, keep needed columns, normalise team names |
| `src/features.py` | Form and Elo features, without look-ahead |
| `src/split.py` | Train/validation/test split by season (§3), run after the features are computed |
| `src/compare_models.py` | Scores the baselines and candidate models on the validation season. Run with `python -m src.compare_models` |
| `src/model.py` | Model definitions |
| `src/train.py` | Train on a split and save the model to `models/` |
| `src/evaluation.py` | Metrics, baselines and the comparison table |
| `src/prediction.py` | Load the saved model and return H/D/A probabilities for a fixture |
| `tests/` | pytest tests, especially no leakage in `features.py` |

The notebook stays for exploration and figures, and imports from `src/` instead of duplicating logic.

## 7. App

- Home page predictor: pick any two **current-season** teams and see H/D/A probabilities.
- Team lists come from the data, not hard-coded. App display names map to data names (e.g. `Man City` → "Manchester City").
- Team pages only for the six featured teams that already have one (decision D8). The other 14 current teams have no page but can be picked in every predictor.
- Deployed on Streamlit Community Cloud.

## 8. Deployment

`data/raw/` is gitignored, so the hosted app has no CSVs. **Decision**: commit the trained model, plus the small table of current ratings and form the app needs, to `models/`. The app then never downloads or trains at startup.

- Split requirements: `requirements.txt` (app only) and `requirements-dev.txt` (jupyter, pytest).

### Model handoff (`models/`)

`train.py` writes these files and `prediction.py` reads them. Agreed on 2026-10-21, so the app can be built before the final model exists.

| File | Written by | Holds |
|---|---|---|
| `models/model.joblib` | `train.py` (T3.6) | The fitted sklearn model, with `predict_proba` |
| `models/team_state.csv` | `train.py` (T3.6) | One row per current-season team, columns `Team,Elo` (decision D7). `Team` uses the **data** names (e.g. `Man City`) |
| `models/features.json` | `train.py` (T3.6) | The list of feature columns, in the order the model expects |

- `prediction.py` builds one row with the columns from `features.json` (e.g. `HomeElo` from the home team's `Elo`) and returns the probabilities as `{"H": ..., "D": ..., "A": ...}`, using `model.classes_` for the order.
- The app maps its display names to data names (T4.2) before looking up `team_state.csv`.

## 9. Security and data

- Public sports data only, with no personal data, so PDPA/GDPR does not apply.
- No secrets are needed. If any appear later, they go in `.streamlit/secrets.toml` (already gitignored), never in code.
- `unsafe_allow_html=True` is only used with fixed strings, never with user input.
- Load model files only from our own repo (pickle/joblib files can run code when loaded).

## 10. Decisions

| ID | Question | Decision (2026-10-16) |
|---|---|---|
| D1 | Use betting odds as a feature, or only as a benchmark? | **Benchmark only**, so the model is our own work. Odds columns are never model inputs |
| D2 | Deadline for the assignment and report? | **Friday 30 October 2026** |
| D3 | How to fill missing form? | **0.79**, as in the notebook |
| D4 | How to handle 2016/17, when ratings and form have no history? | **Warm-up only**: used for Elo and form, left out of training |
| D5 | When are two models' validation log losses "close"? | **A gap under 0.005 is a tie**, and logistic regression wins a tie (agreed 2026-10-21, before seeing any results) |
| D6 | How to parse the mixed date formats? | **`dayfirst=True, format="mixed"`** in `preprocessing.py`, for every season (2026-10-21) |
| D7 | What does `models/team_state.csv` hold? | **`Team,Elo` only**. The chosen model uses `EloDiff` alone, so form is not stored (2026-10-23) |
| D8 | How much frontend do we build? | **Keep the six existing team pages, add no new ones.** All 20 current teams can still be predicted from the home page and team-page dropdowns. The assignment is the ML, so frontend work is kept to the minimum (2026-10-23) |

## 11. Out of scope

Player data, injuries, line-ups, other leagues, live in-match predictions, and predicting exact scores.
