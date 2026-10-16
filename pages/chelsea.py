import streamlit as st
from home import teams

st.set_page_config(
    page_title="Chelsea | Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# =========================
# CHELSEA COLORS
# =========================
CHELSEA_BLUE = "#034694"
DARK_BLUE = "#001489"
LIGHT_BLUE = "#6CABDD"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
BLACK = "#111111"


# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: #034694;
}

/* Back button */
.back-button {
    margin-bottom: 20px;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #034694, #001489);
    padding: 45px;
    border-radius: 20px;
    margin-bottom: 30px;
    color: white;
    box-shadow: 0 6px 18px rgba(0,0,0,0.20);
}

.hero-content h1 {
    color: white !important;
    font-size: 50px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-content p {
    color: white !important;
    font-size: 20px;
    margin-bottom: 0;
}

.team-logo {
    width: 150px;
    margin-bottom: 15px;
}

/* Section titles */
.section-title {
    color: white !important;
    font-size: 30px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 18px;
}

/* Cards */
.info-card,
.metric-card,
.stadium-card,
.history-card,
.predictor-card {
    background: white;
    color: #111111;
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.info-card h3,
.stadium-card h3,
.history-card h3,
.predictor-card h3 {
    color: #034694 !important;
    margin-top: 0;
}

.info-card p,
.stadium-card p,
.history-card p,
.predictor-card p {
    color: #111111 !important;
}

/* Metrics */
.metric-card {
    text-align: center;
}

.metric-label {
    color: #555555;
    font-size: 15px;
    margin-bottom: 8px;
}

.metric-value {
    color: #034694;
    font-size: 32px;
    font-weight: 800;
}

/* Predictor */
.predictor-card {
    border: 3px solid #034694;
}

.predictor-card h2 {
    color: #034694 !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    border-color: #034694 !important;
}

/* Radio */
.stRadio label {
    color: white !important;
}

/* Buttons */
.stButton > button {
    background: white;
    color: #034694;
    border: 2px solid #034694;
    border-radius: 10px;
    font-weight: 700;
    padding: 8px 20px;
}

.stButton > button:hover {
    background: #034694;
    color: white;
}

/* Small gold detail */
.gold-detail {
    color: #D4AF37;
    font-weight: 700;
}

/* Footer */
.footer {
    color: white;
    text-align: center;
    padding: 30px 0;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# BACK BUTTON
# =========================
if st.button("← Back to Home"):
    st.switch_page("home.py")


# =========================
# HERO
# =========================
st.markdown('<div class="hero">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("images/chelsea.png", width=150)

with col2:
    st.markdown('<div class="hero-content">', unsafe_allow_html=True)
    st.markdown("<h1>CHELSEA</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>Premier League Predictor • Match probabilities and team analysis</p>",
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# INTRODUCTION
# =========================
st.markdown(
    '<div class="section-title">About Chelsea</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

<h3>Chelsea Football Club</h3>

<p>
Chelsea FC is one of England's most successful football clubs.
Founded in 1905, the club is based in West London and plays its
home matches at Stamford Bridge.
</p>

<p>
The club is famous for its blue colours and is commonly known as
<strong>The Blues</strong>. Chelsea has enjoyed major success both
domestically and in European competitions.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# TEAM METRICS
# =========================
st.markdown(
    '<div class="section-title">Chelsea at a glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Founded</div>
        <div class="metric-value">1905</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Location</div>
        <div class="metric-value">London</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Nickname</div>
        <div class="metric-value">The Blues</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Stadium</div>
        <div class="metric-value">Stamford Bridge</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# STADIUM
# =========================
st.markdown(
    '<div class="section-title">Stamford Bridge</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="stadium-card">

    <h3>🏟️ Home of Chelsea</h3>

    <p>
    Stamford Bridge has been Chelsea's home since the club was founded
    in 1905. The stadium is located in Fulham, West London.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stadium-card">

    <h3>📍 London</h3>

    <p>
    Stamford Bridge is located in West London and has become one of
    the most recognisable stadiums in English football.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================
# MATCH PREDICTOR
# =========================
st.markdown(
    '<div class="section-title">Match Predictor</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="predictor-card">

<h2>Predict a Chelsea match</h2>

<p>
Choose an opponent and whether Chelsea is playing at home or away.
The prediction model will calculate the probability of a home win,
draw or away win.
</p>

</div>
""", unsafe_allow_html=True)


opponent = st.selectbox(
    "Choose opponent",
    [team[0] for team in teams]
)

home_away = st.radio(
    "Where is the match played?",
    ["Chelsea at home", "Chelsea away"],
    horizontal=True
)

if st.button("Predict Match"):
    st.info(
        f"Prediction for Chelsea vs {opponent} "
        f"({home_away}) will appear here when the model is connected."
    )


# =========================
# CLUB HISTORY
# =========================
st.markdown(
    '<div class="section-title">Club History</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="history-card">

<h3>European success</h3>

<p>
Chelsea have won the UEFA Champions League twice, first in 2012 and
again in 2021. The club has also achieved major success in the
Premier League and domestic cup competitions.
</p>

<h3>2012 Champions League</h3>

<p>
Chelsea won their first Champions League title in 2012 after defeating
Bayern Munich in the final in Munich.
</p>

<h3>2021 Champions League</h3>

<p>
Chelsea won their second Champions League title in 2021 by defeating
Manchester City in the final.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    <span class="gold-detail">⚽</span>
    Premier League Predictor
    <span class="gold-detail">•</span>
    Chelsea
</div>
""", unsafe_allow_html=True)