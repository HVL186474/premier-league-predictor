
from src.prediction import load_artifacts, predict
from src.teams import data_name, teams

import streamlit as st


# -----------------------------
# CSS
# -----------------------------

st.markdown(
    """
    <style>
        /* Main background */
        .stApp {
            background-color: #E34382;
        }

        /* Team cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: white !important;
            border: 1px solid #dddddd !important;
            border-radius: 15px !important;
            padding: 1rem !important;
        }

        /* Text inside white cards */
        div[data-testid="stVerticalBlockBorderWrapper"] h1,
        div[data-testid="stVerticalBlockBorderWrapper"] h2,
        div[data-testid="stVerticalBlockBorderWrapper"] h3,
        div[data-testid="stVerticalBlockBorderWrapper"] p {
            color: #222222 !important;
        }

        /* Hero */
        .hero {
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            background-color: #f5f5f5;
            border: 1px solid #dddddd;
        }

        .hero-small {
            font-size: 0.9rem;
            font-weight: 600;
            color: #666666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .hero-title {
            font-size: 3rem;
            font-weight: 700;
            margin: 0.5rem 0;
            color: #111111;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            color: #666666;
            margin-bottom: 0;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 4rem;
            padding: 1rem;
            color: #eeeeee;
            font-size: 0.9rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Featured teams
# Only these appear on the front page
# -----------------------------

featured_team_names = [
    "Arsenal",
    "Chelsea",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Tottenham",
]

featured_teams = [
    team for team in teams
    if team[0] in featured_team_names
]


# -----------------------------
# Team pages
# -----------------------------

team_pages = {
    "Arsenal": st.Page(
        "pages/arsenal.py",
        title="Arsenal"
    ),

    "Chelsea": st.Page(
        "pages/chelsea.py",
        title="Chelsea"
    ),

    "Liverpool": st.Page(
        "pages/liverpool.py",
        title="Liverpool"
    ),

    "Manchester City": st.Page(
        "pages/mancity.py",
        title="Manchester City"
    ),

    "Manchester United": st.Page(
        "pages/manu.py",
        title="Manchester United"
    ),

    "Tottenham": st.Page(
        "pages/tottenham.py",
        title="Tottenham"
    ),
}


# -----------------------------
# Header
# -----------------------------

st.caption("DAT158 · Machine Learning")

st.title("Premier League Predictor ⚽")

st.write(
    "Predict the outcome of a Premier League match "
    "using machine learning."
)

st.divider()


# -----------------------------
# Match predictor
# All teams available in dropdowns
# -----------------------------

st.subheader("Predict a match")

team_names = [name for name, logo, nickname, _ in teams]

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
        "Home",
        team_names,
        key="home_team"
    )

with col2:
    # Choose a different default away team
    away_index = 1 if len(team_names) > 1 else 0

    away_team = st.selectbox(
        "Away",
        team_names,
        index=away_index,
        key="away_team"
    )

@st.cache_resource
def get_model():
    return load_artifacts()

# -----------------------------
# Prediction button
# -----------------------------

if st.button(
    "Predict",
    use_container_width=True
):
    if home_team == away_team:
        st.warning(
            "Choose different home and away teams."
        )
    else:
        model, ratings = get_model()
        result = predict(model, ratings, data_name[home_team], data_name[away_team])
          
        home_col, draw_col, away_col = st.columns(3)
        home_col.metric(f"{home_team} win", f"{result['H']:.0%}")
        draw_col.metric("Draw", f"{result['D']:.0%}")
        away_col.metric(f"{away_team} win", f"{result['A']:.0%}")
          
        st.caption(
              "Based on each team's current Elo rating. "
              "A draw is almost never the single most likely result, "
              "even though about a quarter of matches end level."
          )


st.divider()


# -----------------------------
# Team cards
# Only six featured teams are shown
# -----------------------------

st.subheader("Premier League Teams")

columns = st.columns(3)

for i, (name, logo, nickname, _) in enumerate(featured_teams):

    with columns[i % 3]:

        with st.container(border=True):

            st.image(
                logo,
                width=150
            )

            st.markdown(f"### {name}")

            st.caption(nickname)

            if st.button(
                f"View {name} →",
                key=f"team_button_{name}",
                use_container_width=True
            ):
                if name in team_pages:
                    st.switch_page(team_pages[name])
                else:
                    st.info(
                        f"The {name} team page has not "
                        "been created yet."
                    )

    # Start a new row after every three teams
    if i % 3 == 2:
        st.write("")


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="footer">
        DAT158 Machine Learning Assignment
        · Premier League Predictor
    </div>
    """,
    unsafe_allow_html=True
)
