
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
# All teams
# Used in dropdown menus
# -----------------------------

teams = [
    ("Arsenal", "images/arsenal.png", "The Gunners"),
    ("Aston Villa", "images/astonvilla.png", "The Villans"),
    ("Bournemouth", "images/bournemouth.png", "The Cherries"),
    ("Brentford", "images/brentford.png", "The Bees"),
    ("Brighton", "images/brighton.png", "The Seagulls"),
    ("Chelsea", "images/chelsea.png", "The Blues"),
    ("Coventry City", "images/coventry.png", "The Sky Blues"),
    ("Crystal Palace", "images/crystalpalace.png", "The Eagles"),
    ("Everton", "images/everton.png", "The Toffees"),
    ("Fulham", "images/fulham.png", "The Cottagers"),
    ("Hull City", "images/hull.png", "The Tigers"),
    ("Ipswich Town", "images/ipswich.png", "The Tractor Boys"),
    ("Leeds United", "images/leeds.png", "The Whites"),
    ("Liverpool", "images/liverpool.png", "The Reds"),
    ("Manchester City", "images/mancity.png", "The Citizens"),
    ("Manchester United", "images/manu.png", "The Red Devils"),
    ("Newcastle United", "images/newcastle.png", "The Magpies"),
    ("Nottingham Forest", "images/nottingham.png", "The Tricky Trees"),
    ("Tottenham", "images/spurs.png", "Spurs")
]


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

team_names = [name for name, logo, nickname in teams]

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
        st.info(
            f"Prediction for **{home_team}** vs "
            f"**{away_team}** coming soon..."
        )


st.divider()


# -----------------------------
# Team cards
# Only six featured teams are shown
# -----------------------------

st.subheader("Premier League Teams")

columns = st.columns(3)

for i, (name, logo, nickname) in enumerate(featured_teams):

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
