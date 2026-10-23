import streamlit as st
from src.teams import teams

st.set_page_config(
    page_title="Tottenham | Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# =========================
# COLORS
# =========================

SPURS_BLUE = "#132257"
LIGHT_BLUE = "#4A90E2"
DARK_BLUE = "#07133A"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
BLACK = "#111111"


# =========================
# PAGE CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: #07133A;
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
        #132257 0%,
        #132257 55%,
        #07133A 100%
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

    color: #132257 !important;
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

    border-top: 5px solid #4A90E2;
}

.metric-label {
    color: #555555;
    font-size: 15px;
    margin-bottom: 8px;
}

.metric-value {
    color: #132257;
    font-size: 30px;
    font-weight: 800;
}


/* =========================
   PREDICTOR
   ========================= */

.predictor-card {
    border: 3px solid #4A90E2;
}

.predictor-card h2 {
    color: #132257 !important;
}


/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {
    border-color: #4A90E2 !important;
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
    color: #132257;

    border: 2px solid #4A90E2;
    border-radius: 10px;

    font-weight: 700;

    padding: 8px 20px;
}

.stButton > button:hover {

    background: #4A90E2;
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
    color: #D4AF37;
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
    st.image("images/spurs.png", width=150)

with col2:

    st.markdown(
        '<div class="hero-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1>TOTTENHAM HOTSPUR</h1>",
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
# ABOUT TOTTENHAM
# =========================

st.markdown(
    '<div class="section-title">About Tottenham Hotspur</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

<h3>Tottenham Hotspur Football Club</h3>

<p>
Tottenham Hotspur is an English football club based in North London.
Founded in 1882, the club plays its home matches at Tottenham Hotspur
Stadium.
</p>

<p>
Tottenham are famous for their white shirts and are commonly known as
<strong>Spurs</strong>. The club has a long history in English football
and has competed at the highest level of the Premier League for many years.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# QUICK FACTS
# =========================

st.markdown(
    '<div class="section-title">Tottenham at a glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Founded</div>
        <div class="metric-value">1882</div>
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
        <div class="metric-value">Spurs</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Stadium</div>
        <div class="metric-value">Tottenham Hotspur Stadium</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# TOTTENHAM HOTSPUR STADIUM
# =========================

st.markdown(
    '<div class="section-title">Tottenham Hotspur Stadium</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="stadium-card">

    <h3>🏟️ Home of Spurs</h3>

    <p>
    Tottenham Hotspur Stadium opened in 2019 and replaced White Hart Lane
    as the club's home ground. It is one of the most modern football
    stadiums in Europe.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="stadium-card">

    <h3>⚪ The Lilywhites</h3>

    <p>
    Tottenham are traditionally associated with white shirts and are
    known by the nickname "The Lilywhites". The club's supporters create
    a strong atmosphere at home matches.
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

<h2>Predict a Tottenham match</h2>

<p>
Choose an opponent and whether Tottenham is playing at home or away.
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
    [
        "Tottenham at home",
        "Tottenham away"
    ],
    horizontal=True
)

if st.button("Predict Match"):

    st.info(
        f"Prediction for Tottenham vs {opponent} "
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

<h3>Founded in 1882</h3>

<p>
Tottenham Hotspur were founded in 1882 and have developed into one of
the most recognisable football clubs in England.
</p>


<h3>White Hart Lane</h3>

<p>
For more than a century, White Hart Lane was Tottenham's famous home.
The stadium became an important part of the club's identity before
being replaced by the new Tottenham Hotspur Stadium.
</p>


<h3>1961 Double</h3>

<p>
Tottenham had one of the greatest seasons in English football in
1960/61, winning both the First Division title and the FA Cup.
</p>


<h3>European success</h3>

<p>
Tottenham won the UEFA Cup in 1972 and again in 1984. The club also
reached the UEFA Champions League final in 2019.
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
Tottenham Hotspur

</div>
""", unsafe_allow_html=True)