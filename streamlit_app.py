import streamlit as st


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)


# -----------------------------
# Pages
# -----------------------------

pages = {
    "": [
        st.Page(
            "home.py",
            title="Home",
            default=True
        )
    ],

    "Teams": [
        st.Page(
            "pages/arsenal.py",
            title="Arsenal"
        ),
        st.Page(
            "pages/chelsea.py",
            title="Chelsea"
        ),
        st.Page(
            "pages/liverpool.py",
            title="Liverpool"
        ),
        st.Page(
            "pages/mancity.py",
            title="Manchester City"
        ),
        st.Page(
            "pages/manu.py",
            title="Manchester United"
        ),
        st.Page(
            "pages/tottenham.py",
            title="Tottenham"
        )
    ]
}


# -----------------------------
# Navigation
# -----------------------------

pg = st.navigation(
    pages,
    position="hidden"
)


# -----------------------------
# Run selected page
# -----------------------------

pg.run()