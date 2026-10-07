import streamlit as st
from home import teams

# -----------------------------
# CSS
# -----------------------------

st.markdown(
    """
    <style>

        /* Main background */

        .stApp {
            background-color: darkgreen;
        }


        /* Team cards */

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: white !important;
            border: 1px solid #dddddd !important;
            border-radius: 15px !important;
            padding: 1rem !important;
        }


        /* Text inside cards */

        div[data-testid="stVerticalBlockBorderWrapper"] h1,
        div[data-testid="stVerticalBlockBorderWrapper"] h2,
        div[data-testid="stVerticalBlockBorderWrapper"] h3,
        div[data-testid="stVerticalBlockBorderWrapper"] p {
            color: black !important;
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
# Teams
# -----------------------------

teams = [
    ("Arsenal", "images/arsenal.png", "The Gunners"),
    ("Chelsea", "images/chelsea.png", "The Blues"),
    ("Liverpool", "images/liverpool.png", "The Reds"),
    ("Manchester City", "images/mancity.png", "The Citizens"),
    ("Manchester United", "images/manu.png", "The Red Devils"),
    ("Tottenham", "images/spurs.png", "Spurs")
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
    )
}


# =========================================================
# HEADER
# =========================================================

st.caption("DAT158 · Machine Learning")

st.title("Premier League Predictor ⚽")

st.write(
    "Predict the outcome of a Premier League match "
    "using machine learning."
)

st.divider()


# =========================================================
# MATCH PREDICTOR
# =========================================================

st.subheader("Predict a match")


team_names = [
    "Arsenal",
    "Chelsea",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Tottenham"
]


# -----------------------------
# Team selection
# -----------------------------

col1, col2 = st.columns(2)


with col1:

    home_team = st.selectbox(
        "Home",
        team_names
    )


with col2:

    away_team = st.selectbox(
        "Away",
        team_names
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
            f"Prediction for {home_team} "
            f"vs {away_team} coming soon..."
        )


st.divider()


# =========================================================
# TEAM CARDS
# =========================================================

st.subheader("Premier League Teams")


columns = st.columns(3)


for i, (name, logo, nickname) in enumerate(teams):

    with columns[i % 3]:

        with st.container(border=True):

            st.image(
                logo,
                width=150
            )

            st.markdown(
                f"### {name}"
            )

            st.caption(
                nickname
            )


            # -----------------------------
            # Team page button
            # -----------------------------

            if st.button(
                f"View {name} →",
                key=f"team_button_{name}",
                use_container_width=True
            ):

                st.switch_page(
                    team_pages[name]
                )


    # -----------------------------
    # New row after 3 teams
    # -----------------------------

    if i == 2:

        st.write("")

        columns = st.columns(3)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        DAT158 Machine Learning Assignment
        · Premier League Predictor

    </div>
    """,
    unsafe_allow_html=True
)