import streamlit as st
from datetime import date
st.markdown("""
<style>

    /* Sfondo */
    .stApp {
        background-color: #fff0f5;
    }

    /* Titolo principale */
    h1 {
        color: #d63384;
        text-align: center;
        font-family: Georgia, serif;
    }

    /* Titoli delle sezioni */
    h2, h3 {
        color: #c2185b;
        font-family: Georgia, serif;
    }

    /* Testo */
    p {
        color: #5c3a46;
        font-size: 17px;
        line-height: 1.7;
    }

    /* Immagini arrotondate */
    .stImage img {
        border-radius: 20px;
    }

    /* Divider */
    hr {
        border-color: #f3b6cc;
    }

    /* Pulsanti */
    .stButton > button {
        background-color: #d63384;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 25px;
        font-size: 16px;
    }

    .stButton > button:hover {
        background-color: #c2185b;
        color: white;
    }

</style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="Buon Compleanno tato 🩷", page_icon= "🎂")
st.title("Tanti auguri amore mio 💕  🎂🎂")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("yahya.jpeg", caption="Noi due <3", width=300)
st.audio("Paramore_StillIntoYou.mp3")
st.balloons()
st.divider()
st.markdown("""
### Ciao Amore,
Oggi compi 22 anni, ormai sei un uomo adulto, e sono davvero contenta di sapere che ho di fianco a me una persona fantastica come te.
Sono fiera di te, di quello che sei e quello che diventerai. Non vedo l'ora di passare la vita con te, vederti crescere con me sarebbe un sogno.

Immagino le domeniche a riposarci insieme, a coccolarci, ma anche fare la spesa, pulire la casa insieme.

Immagino le sere dopo le lunghe giornate a lavoro, ad abbracciarci, a consolarci e soprattutto a ridere insieme.

Spero di poter avere il privilegio di passare la mia vita con te.

Ti auguro il meglio amore mio

**Ti amo**

*la tua Giada*
""")
data_inizio = date(2026, 9, 3)
oggi = date.today()

giorni = (oggi - data_inizio).days
data_risentiti = date(2026, 1, 29)
giorni_risentiti = (date.today() - data_risentiti).days

st.markdown(f"""
### 💌 Ci risentiamo da {giorni_risentiti} giorni
### ❤️ Insieme da {giorni} giorni ❤️

E spero che questi siano solo i primi di tantissimi.
""")
st.divider()

st.markdown(
    "<h2 style='text-align:center;'>🏡 Il nostro futuro</h2>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
    background-color:#ffe0eb;
    padding:25px;
    border-radius:20px;
">

<p>Vorrei...</p>

<p>🛒 Fare la spesa insieme la domenica</p>

<p>🍝 Cucinare insieme</p>

<p>🛋️ Passare le serate abbracciati sul divano</p>

<p>✈️ Viaggiare insieme</p>

<p>🏡 Costruire una casa tutta nostra</p>

<p>❤️ E soprattutto continuare a stare con te ogni giorno.</p>

</div>
""", unsafe_allow_html=True)

with st.expander("💌 C'è una cosa che voglio dirti..."):
    st.write("""
    Se sei arrivato fin qui, sappi che sceglierei te altre mille volte.
    In qualsiasi vita, in qualsiasi momento,
    spero di ritrovarti sempre.
    
    Buon compleanno amore mio ❤️
    """)
