import streamlit as st
from src.teams import teams

st.set_page_config(
    page_title="Manchester United | Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# =========================
# COLORS
# =========================

RED = "#DA291C"
DARK_RED = "#B71C1C"
DEEP_RED = "#8B0000"
GOLD = "#FBE122"
WHITE = "#FFFFFF"
BLACK = "#111111"


# =========================
# PAGE CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: #8B0000;
}

.block-container {
    max-width: 100%;
    padding-left: 4rem;
    padding-right: 4rem;
}


/* =========================
   HERO
   ========================= */

.hero {
    background: linear-gradient(
        135deg,
        #DA291C 0%,
        #DA291C 55%,
        #8B0000 100%
    );

    padding: 45px;
    border-radius: 20px;
    margin-bottom: 30px;

    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
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


/* =========================
   SECTION TITLES
   ========================= */

.section-title {
    color: white !important;
    font-size: 30px;
    font-weight: 800;

    margin-top: 30px;
    margin-bottom: 18px;
}


/* =========================
   CARDS
   ========================= */

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

    box-shadow: 0 4px 12px rgba(0,0,0,0.18);
}


/* =========================
   CARD HEADINGS
   ========================= */

.info-card h3,
.stadium-card h3,
.history-card h3,
.predictor-card h3 {

    color: #DA291C !important;
    margin-top: 0;
}


/* =========================
   CARD TEXT
   ========================= */

.info-card p,
.stadium-card p,
.history-card p,
.predictor-card p {

    color: #111111 !important;
    line-height: 1.6;
}


/* =========================
   METRIC CARDS
   ========================= */

.metric-card {
    text-align: center;
    min-height: 120px;

    border-top: 5px solid #DA291C;
}

.metric-label {
    color: #555555;
    font-size: 15px;
    margin-bottom: 8px;
}

.metric-value {
    color: #DA291C;
    font-size: 30px;
    font-weight: 800;
}


/* =========================
   PREDICTOR
   ========================= */

.predictor-card {
    border: 3px solid #DA291C;
}

.predictor-card h2 {
    color: #DA291C !important;
}


/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {
    border-color: #DA291C !important;
}


/* =========================
   RADIO
   ========================= */

.stRadio label {
    color: white !important;
}


/* =========================
   BUTTON
   ========================= */

.stButton > button {

    background: white;
    color: #DA291C;

    border: 2px solid #DA291C;
    border-radius: 10px;

    font-weight: 700;

    padding: 8px 20px;
}

.stButton > button:hover {

    background: #DA291C;
    color: white;
}


/* =========================
   FOOTER
   ========================= */

.footer {
    color: white;
    text-align: center;

    padding: 30px 0;

    font-size: 14px;
}

.gold-detail {
    color: #FBE122;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# =========================
# BACK TO HOME
# =========================

if st.button("← Back to Home"):
    st.switch_page("home.py")


# =========================
# HERO
# =========================

st.markdown('<div class="hero">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])

with col1:
    st.image("images/manu.png", width=150)

with col2:

    st.markdown(
        '<div class="hero-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1>MANCHESTER UNITED</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p>Premier League Predictor • Match probabilities and team analysis</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# ABOUT MANCHESTER UNITED
# =========================

st.markdown(
    '<div class="section-title">About Manchester United</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

<h3>Manchester United Football Club</h3>

<p>
Manchester United is one of the most famous and successful football clubs
in English football. Founded in 1878, the club is based in Manchester and
plays its home matches at Old Trafford.
</p>

<p>
The club is famous for its red colours and is commonly known as
<strong>The Red Devils</strong>. Manchester United has a long history of
success in the Premier League, FA Cup and European competitions.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# QUICK FACTS
# =========================

st.markdown(
    '<div class="section-title">Manchester United at a glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Founded</div>
        <div class="metric-value">1878</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Location</div>
        <div class="metric-value">Manchester</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Nickname</div>
        <div class="metric-value">Red Devils</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Stadium</div>
        <div class="metric-value">Old Trafford</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# OLD TRAFFORD
# =========================

st.markdown(
    '<div class="section-title">Old Trafford</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="stadium-card">

    <h3>🏟️ The Theatre of Dreams</h3>

    <p>
    Old Trafford has been Manchester United's home since 1910.
    The stadium is one of the most recognisable football grounds
    in England and is famously known as the "Theatre of Dreams".
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="stadium-card">

    <h3>🔴 Home of the Red Devils</h3>

    <p>
    Old Trafford has hosted many historic Manchester United matches
    and is known for its passionate supporters and famous red
    atmosphere on matchdays.
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

<h2>Predict a Manchester United match</h2>

<p>
Choose an opponent and whether Manchester United is playing at home
or away. The prediction model will calculate the probability of a
home win, draw or away win.
</p>

</div>
""", unsafe_allow_html=True)

opponent = st.selectbox(
    "Choose opponent",
     [team[0] for team in teams]
)

home_away = st.radio(
    "Where is the match played?",
    [
        "Manchester United at home",
        "Manchester United away"
    ],
    horizontal=True
)

if st.button("Predict Match"):

    st.info(
        f"Prediction for Manchester United vs {opponent} "
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

<h3>One of England's most successful clubs</h3>

<p>
Manchester United have won numerous domestic and international trophies
and are one of the most successful clubs in English football history.
</p>


<h3>The Sir Alex Ferguson era</h3>

<p>
Sir Alex Ferguson managed Manchester United from 1986 until 2013.
During his time at the club, United became one of the dominant forces
in English football and won numerous trophies.
</p>


<h3>The 1998/99 Treble</h3>

<p>
The 1998/99 season became one of the greatest seasons in Manchester
United's history. The club won the Premier League, FA Cup and UEFA
Champions League to complete a historic treble.
</p>


<h3>Premier League dominance</h3>

<p>
Manchester United have won the Premier League many times and have
played a major role in the history of the competition since its
formation in 1992.
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
Manchester United

</div>
""", unsafe_allow_html=True)