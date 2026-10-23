# Tasks

Work items for the [Blueprint](BLUEPRINT.md). Every code change should map to a task here. Tick a task off when it is merged.

**Deadline**: Friday 30 October 2026 (decision D2). Target dates leave 29–30 October as buffer.

## Run-in schedule (agreed 2026-10-21, synced 2026-10-23)

| Day | Alexander | Andreas |
|---|---|---|
| Fri 23 | Commit T3.3 (K = 30) with tests fixed. Start report R1 | T2.7 `score()` to §3 spec, T3.4 gradient boosting. Then together: pick model (D5), run T3.5 once |
| Sat 24 | T3.6 save model to `models/`, push. Report R2 | Blocked on `models/` until it lands; T2.1, T2.3, T4.2 meanwhile |
| Sun 25 – Mon 26 | Report | T4.1, T4.3, T4.4 |
| Tue 27 | Report | T5.1, T5.2 deploy |
| Wed 28 | QA + code freeze together. Report final draft | Same |
| Thu 29 | Reports done (individual) | Same |
| Fri 30 | Submit | Submit |

## Phase 1: Plan (by Sat 17 Oct)

- [x] **T1.1** Write `docs/BLUEPRINT.md` and `docs/task.md`
- [ ] **T1.2** Teammate reviews the blueprint and confirms decisions D1 and D2

## Phase 2: Move the notebook logic into `src/` (Sat 17 – Tue 20 Oct)

- [ ] **T2.1** Add `requirements-dev.txt` with pytest and jupyter, and remove jupyter from `requirements.txt`
- [ ] **T2.2** `data_loader.py`: use paths relative to the project root, and drop the `os.chdir("..")` from the notebook
- [ ] **T2.3** `preprocessing.py`: parse dates, sort by date, keep only needed columns
- [x] **T2.4** `features.py`: form feature, filling missing form with 0.79 (decision D3)
- [x] **T2.5** `features.py`: Elo feature
- [x] **T2.6** `tests/test_features.py`: no look-ahead (changing a match's result must not change its own features), correct form values on a small hand-made example, Elo ratings sum unchanged after a match
- [x] **T2.7** `evaluation.py`: log loss, accuracy, confusion matrix, and the baseline table from the blueprint
- [ ] **T2.8** Notebook imports from `src/` instead of defining the logic inline

## Phase 3: Improve the model (Wed 21 – Sat 24 Oct)

- [x] **T3.1** Train/validation/test split by season, with 2016/17 as warm-up only (blueprint §3, decision D4)
- [x] **T3.2** Logistic regression on Elo + form. Compare against baselines on validation data
- [x] **T3.3** Try the candidate features from blueprint §4. Keep only what lowers validation log loss
- [x] **T3.4** Gradient-boosted model for comparison
- [x] **T3.5** Final test-set evaluation (run once) plus figures for the report
- [x] **T3.6** `train.py`: retrain the chosen model on all completed seasons and save it to `models/`

## Phase 4: Connect the app (Sun 25 – Mon 26 Oct)

- [ ] **T4.1** `prediction.py`: load the model and current team ratings, return H/D/A probabilities
- [ ] **T4.2** Map team names between the app and the data
- [ ] **T4.3** Home page: build the team list from current-season data and show probabilities
- [ ] **T4.4** The six existing team pages: build the opponent list from the data and show probabilities. No new pages (decision D8)

## Phase 5: Deploy (Tue 27 Oct)

- [ ] **T5.1** Commit the model files and make sure the app runs with an empty `data/raw/`
- [ ] **T5.2** Deploy to Streamlit Community Cloud and smoke-test it

## Phase 6: Clean up (optional, only if time allows)

- [ ] ~~**T6.1** Replace the six team pages with one shared template plus per-team content~~ Dropped (decision D8)
- [ ] **T6.2** Remove the duplicate `team_pages` setup in `home.py`
- [ ] **T6.3** Replace deprecated `use_container_width` arguments

## Report (write alongside phases 3–5, final draft by Wed 28 Oct)

- [ ] **R1** Data and features section (include the leakage rules)
- [ ] **R2** Results table against the baselines, and a discussion of draws
- [ ] **R3** App description with screenshots
