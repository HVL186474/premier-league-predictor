# premier-league-predictor
DAT158 ML assignment 2: Premier League match result predictor (Streamlit)

Pick a home team and an away team, and the app gives the probability of a home win, a draw and an away win. The model is a logistic regression on the Elo rating difference between the teams.

- **Live app**: https://beste-dat158-prosjekt.streamlit.app/
- **Report**: [docs/DAT158-rapport.pdf](docs/DAT158-rapport.pdf)

## Run the app

Developed with Python 3.14. The trained model is committed in `models/`, so the app needs no data download.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
streamlit run streamlit_app.py
```

## Reproduce the results

Run these from the project root:

```bash
python -m src.data_loader       # download the season files to data/raw/
python -m src.compare_models    # model comparison on the validation season (2024/25)
python -m src.final_evaluation  # final numbers on the test season (2025/26), writes figures/
python -m src.train             # retrain on all completed seasons, writes models/
pytest                          # run the tests
```

The downloaded file for the current season grows as matches are played. The validation and test numbers use completed seasons only, but the team ratings written by `src.train` will change. The committed `models/` were built with 50 matches of 2026/27.

## Project documents

- [Blueprint](docs/BLUEPRINT.md): the agreed spec (data, features, evaluation, app, deployment).
- [Tasks](docs/task.md): the work breakdown. Every code change maps to a task here.
- [Report notes](docs/report-notes.md): the measured numbers and findings behind the report.
