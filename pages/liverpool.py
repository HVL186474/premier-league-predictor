import streamlit as st

st.set_page_config(
    page_title="Liverpool | Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# =========================
# LIVERPOOL COLORS
# =========================
LIVERPOOL_RED = "#C8102E"
DARK_RED = "#8B0000"
DEEP_RED = "#7A0019"
GREEN = "#006A4E"
DARK_GREEN = "#064B3C"
GOLD = "#F6C343"
WHITE = "#FFFFFF"
BLACK = "#111111"


# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: #8B0000;
}

/* Full width */
.block-container {
    max-width: 100%;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* Back button */
.back-button {
    margin-bottom: 20px;
}

/* =========================
   HERO
   ========================= */

.hero {
    background: linear-gradient(
        135deg,
        #C8102E 0%,
        #C8102E 60%,
        #8B0000 100%
    );

    padding: 45px;
    border-radius: 20px;
    margin-bottom: 30px;

    color: white;

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

.team-logo {
    width: 150px;
    margin-bottom: 15px;
}


/* =========================
   SECTION TITLES
   ========================= */

.section-title {
    color: #F6C343 !important;
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


/* Card headings */

.info-card h3,
.stadium-card h3,
.history-card h3,
.predictor-card h3 {

    color: #C8102E !important;

    margin-top: 0;
}


/* Card text */

.info-card p,
.stadium-card p,
.history-card p,
.predictor-card p {

    color: #111111 !important;

    line-height: 1.6;
}


/* =========================
   METRICS
   ========================= */

.metric-card {

    text-align: center;

    min-height: 120px;

    border-top: 5px solid #C8102E;
}

.metric-label {

    color: #555555;

    font-size: 15px;

    margin-bottom: 8px;
}

.metric-value {

    color: #C8102E;

    font-size: 30px;

    font-weight: 800;
}


/* =========================
   PREDICTOR
   ========================= */

.predictor-card {

    border: 3px solid #C8102E;
}

.predictor-card h2 {

    color: #C8102E !important;
}


/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {

    border-color: #C8102E !important;
}


/* =========================
   RADIO
   ========================= */

.stRadio label {

    color: white !important;
}


/* =========================
   BUTTONS
   ========================= */

.stButton > button {

    background: white;

    color: #C8102E;

    border: 2px solid #C8102E;

    border-radius: 10px;

    font-weight: 700;

    padding: 8px 20px;
}

.stButton > button:hover {

    background: #C8102E;

    color: white;
}


/* =========================
   SMALL GREEN DETAIL
   ========================= */

.green-detail {

    color: #006A4E;

    font-weight: 700;
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

    color: #F6C343;

    font-weight: 700;
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
    st.image("images/liverpool.png", width=150)

with col2:

    st.markdown(
        '<div class="hero-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1>LIVERPOOL</h1>",
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
# ABOUT
# =========================

st.markdown(
    '<div class="section-title">About Liverpool</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

<h3>Liverpool Football Club</h3>

<p>
Liverpool FC is one of the most successful and historic football clubs
in England. Founded in 1892, the club is based in Liverpool and plays
its home matches at the iconic Anfield stadium.
</p>

<p>
Liverpool are famous for their red colours and are commonly known as
<strong>The Reds</strong>. The club has a long history of success in
English football and European competitions.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# TEAM METRICS
# =========================

st.markdown(
    '<div class="section-title">Liverpool at a glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Founded</div>
        <div class="metric-value">1892</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Location</div>
        <div class="metric-value">Liverpool</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Nickname</div>
        <div class="metric-value">The Reds</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Stadium</div>
        <div class="metric-value">Anfield</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# ANFIELD
# =========================

st.markdown(
    '<div class="section-title">Anfield</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="stadium-card">

    <h3>🏟️ Home of Liverpool</h3>

    <p>
    Anfield has been Liverpool's home since the club was founded
    in 1892. The stadium is famous around the world for its
    atmosphere and passionate supporters.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="stadium-card">

    <h3>🎵 You'll Never Walk Alone</h3>

    <p>
    Liverpool supporters famously sing "You'll Never Walk Alone"
    before matches, making the atmosphere at Anfield one of the
    most recognisable in football.
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

<h2>Predict a Liverpool match</h2>

<p>
Choose an opponent and whether Liverpool is playing at home or away.
The prediction model will calculate the probability of a home win,
draw or away win.
</p>

</div>
""", unsafe_allow_html=True)


opponents = [
    "Arsenal",
    "Aston Villa",
    "Brighton",
    "Brentford",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Leeds United",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Tottenham",
    "West Ham",
    "Wolves"
]

opponent = st.selectbox(
    "Choose opponent",
    opponents
)

home_away = st.radio(
    "Where is the match played?",
    ["Liverpool at home", "Liverpool away"],
    horizontal=True
)

if st.button("Predict Match"):

    st.info(
        f"Prediction for Liverpool vs {opponent} "
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
Liverpool have a long history of success in European football.
The club has won the UEFA Champions League six times, making it
one of the most successful English clubs in the competition.
</p>

<h3>1980s dominance</h3>

<p>
Liverpool enjoyed a particularly successful period during the
1970s and 1980s, winning numerous domestic league titles and
European trophies.
</p>

<h3>2019 Champions League</h3>

<p>
Liverpool won the Champions League in 2019 after defeating
Tottenham Hotspur in the final in Madrid.
</p>

<h3>Premier League era</h3>

<p>
Liverpool won their first Premier League title in the 2019/20
season, ending a long wait for the English top-flight championship.
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

    Liverpool

</div>
""", unsafe_allow_html=True)