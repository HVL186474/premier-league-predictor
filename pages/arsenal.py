import streamlit as st
from src.teams import teams
from src.prediction_view import show_prediction

st.set_page_config(
    page_title="Arsenal | Premier League Predictor",
    page_icon="⚽",
    layout="wide"
)

# =========================
# COLORS
# =========================

ARSENAL_RED = "#DB0007"
DARK_RED = "#9C0006"
DEEP_RED = "#650003"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
BLACK = "#111111"


# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: #650003;
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
        #DB0007 0%,
        #DB0007 60%,
        #9C0006 100%
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


/* =========================
   CARD HEADINGS
   ========================= */

.info-card h3,
.stadium-card h3,
.history-card h3,
.predictor-card h3 {

    color: #DB0007 !important;
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
   METRICS
   ========================= */

.metric-card {
    text-align: center;
    min-height: 120px;

    border-top: 5px solid #DB0007;
}

.metric-label {
    color: #555555;
    font-size: 15px;
    margin-bottom: 8px;
}

.metric-value {
    color: #DB0007;
    font-size: 30px;
    font-weight: 800;
}


/* =========================
   PREDICTOR
   ========================= */

.predictor-card {
    border: 3px solid #DB0007;
}

.predictor-card h2 {
    color: #DB0007 !important;
}


/* =========================
   SELECTBOX
   ========================= */

div[data-baseweb="select"] > div {
    border-color: #DB0007 !important;
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
    color: #DB0007;

    border: 2px solid #DB0007;
    border-radius: 10px;

    font-weight: 700;

    padding: 8px 20px;
}

.stButton > button:hover {

    background: #DB0007;
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
    st.image("images/arsenal.png", width=150)

with col2:

    st.markdown(
        '<div class="hero-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1>ARSENAL</h1>",
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
# ABOUT ARSENAL
# =========================

st.markdown(
    '<div class="section-title">About Arsenal</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

<h3>Arsenal Football Club</h3>

<p>
Arsenal Football Club was founded in 1886 and is based in North London.
The club plays its home matches at the Emirates Stadium.
</p>

<p>
Arsenal are famous for their red and white colours and are commonly
known as <strong>The Gunners</strong>. The club has a long history in
English football and has been a regular competitor at the top level
of the Premier League.
</p>

</div>
""", unsafe_allow_html=True)


# =========================
# ARSENAL AT A GLANCE
# =========================

st.markdown(
    '<div class="section-title">Arsenal at a glance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Founded</div>
        <div class="metric-value">1886</div>
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
        <div class="metric-value">The Gunners</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Stadium</div>
        <div class="metric-value">Emirates Stadium</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# EMIRATES STADIUM
# =========================

st.markdown(
    '<div class="section-title">Emirates Stadium</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="stadium-card">

    <h3>🏟️ Home of Arsenal</h3>

    <p>
    The Emirates Stadium has been Arsenal's home since 2006.
    It replaced Highbury and is located in North London.
    The stadium is one of the most recognisable football grounds
    in England.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="stadium-card">

    <h3>🔴 The Gunners</h3>

    <p>
    Arsenal's traditional red and white colours are a major part
    of the club's identity. The nickname "The Gunners" reflects
    the club's historical connection to the Royal Arsenal.
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

<h2>Predict an Arsenal match</h2>

<p>
Choose an opponent and whether Arsenal is playing at home or away.
The prediction model will calculate the probability of a home win,
draw or away win.
</p>

</div>
""", unsafe_allow_html=True)




opponent = st.selectbox(
    "Choose opponent",
    [team[0] for team in teams if team[0] != "Arsenal"]
)

home_away = st.radio(
    "Where is the match played?",
    ["Arsenal at home", "Arsenal away"],
    horizontal=True
)

if st.button("Predict Match"):
    if home_away == "Arsenal at home":
        show_prediction("Arsenal", opponent)
    else:
        show_prediction(opponent, "Arsenal")


# =========================
# CLUB HISTORY
# =========================

st.markdown(
    '<div class="section-title">Arsenal History</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="history-card">

<h3>1998/99</h3>

<p>
Arsenal finished second in the Premier League behind Manchester United.
It was the beginning of a period where Arsenal regularly challenged
for the title.
</p>


<h3>1999/00</h3>

<p>
Arsenal again finished second behind Manchester United after another
strong Premier League campaign.
</p>


<h3>2000/01</h3>

<p>
For the third consecutive season, Arsenal finished second in the
Premier League, once again behind Manchester United.
</p>


<h3>2002/03</h3>

<p>
Arsenal finished second behind Manchester United before going on to
win the Premier League the following season.
</p>


<h3>2004/05</h3>

<p>
Arsenal finished second behind Chelsea during the 2004/05 Premier
League season.
</p>


<h3>2015/16</h3>

<p>
Arsenal finished second behind Leicester City in one of the most
unexpected Premier League title races in history.
</p>


<h3>2022/23</h3>

<p>
Arsenal finished second behind Manchester City after spending much
of the season competing for the Premier League title.
</p>


<h3>2023/24</h3>

<p>
Arsenal again finished second behind Manchester City after another
very close Premier League title race.
</p>


<h3>2024/25</h3>

<p>
Arsenal finished second for the third consecutive season, continuing
their run of challenging for the Premier League title.
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
Arsenal

</div>
""", unsafe_allow_html=True)