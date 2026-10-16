import streamlit as st
from home import teams

st.set_page_config(
    page_title="Manchester City | Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# =========================
# MANCHESTER CITY COLORS
# =========================
CITY_BLUE = "#6CABDD"
DARK_BLUE = "#0B1C2C"
DEEP_BLUE = "#003B5C"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
BLACK = "#111111"


# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: #003B5C;
}

/* Full width */
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
        #6CABDD 0%,
        #4F9BD1 60%,
        #003B5C 100%
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


/* Card headings */

.info-card h3,
.stadium-card h3,
.history-card h3,
.predictor-card h3 {

    color: #003B5C !important;

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

    border-top: 5px solid #6CABDD;
}

.metric-label {

    color: #555555;

    font-size: 15px;

    margin-bottom: 8px;
}

.metric-value {

    color: #003B5C;

    font-size: 30px;

    font-weight: 800;
}


/* =========================
   PREDICTOR
   ========================= */

.predictor-card {

    border: 3px solid #6CABDD;
}

.predictor-card h2 {

    color: #003B5C !important;
}


/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {

    border-color: #6CABDD !important;
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

    color: #003B5C;

    border: 2px solid #6CABDD;

    border-radius: 10px;

    font-weight: 700;

    padding: 8px 20px;
}

.stButton > button:hover {

    background: #6CABDD;

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
    st.image("images/mancity.png", width=150)

with col2:

    st.markdown(
        '<div class="hero-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1>MANCHESTER CITY</h1>",
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
    '<div class="section-title">About Manchester City</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

<h3>Manchester City Football Club</h3>

<p>
Manchester City FC is one of the most successful clubs in modern
English football. Founded in 1880, the club is based in Manchester
and plays its home matches at the Etihad Stadium.
</p>

<p>
Manchester City are famous for their sky-blue colours and are
commonly known as <strong>The Citizens</strong>. The club has enjoyed
major success in the Premier League, domestic competitions and
European football.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# TEAM METRICS
# =========================

st.markdown(
    '<div class="section-title">Manchester City at a glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Founded</div>
        <div class="metric-value">1880</div>
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
        <div class="metric-value">The Citizens</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Stadium</div>
        <div class="metric-value">Etihad Stadium</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# ETIHAD STADIUM
# =========================

st.markdown(
    '<div class="section-title">Etihad Stadium</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="stadium-card">

    <h3>🏟️ Home of Manchester City</h3>

    <p>
    The Etihad Stadium has been Manchester City's home since 2003.
    It is located in the east of Manchester and has become one of
    the most recognisable stadiums in English football.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="stadium-card">

    <h3>🔵 The Citizens</h3>

    <p>
    Manchester City's sky-blue colours have become one of the most
    recognisable identities in the Premier League. The supporters
    are known for creating a strong atmosphere on matchdays.
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

<h2>Predict a Manchester City match</h2>

<p>
Choose an opponent and whether Manchester City is playing at home
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
    ["Manchester City at home", "Manchester City away"],
    horizontal=True
)

if st.button("Predict Match"):

    st.info(
        f"Prediction for Manchester City vs {opponent} "
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

<h3>Premier League success</h3>

<p>
Manchester City have become one of the dominant teams in English
football, particularly during the modern Premier League era.
The club has won multiple Premier League titles.
</p>

<h3>2012 Premier League title</h3>

<p>
Manchester City won the Premier League in dramatic fashion in 2012,
securing the title with a last-minute goal against Queens Park Rangers
on the final day of the season.
</p>

<h3>2023 Treble</h3>

<p>
The 2022/23 season became one of the greatest in Manchester City's
history. The club won the Premier League, FA Cup and UEFA Champions
League to complete a historic treble.
</p>

<h3>European champions</h3>

<p>
Manchester City won their first UEFA Champions League title in 2023,
defeating Inter Milan in the final in Istanbul.
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

    Manchester City

</div>
""", unsafe_allow_html=True)