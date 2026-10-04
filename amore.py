import streamlit as st
from datetime import date
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #d63384;
}

h2, h3 {
    color: #c2185b;
}

.stImage img {
    border-radius: 15px;
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

st.header("🏡 Il nostro futuro")

st.markdown("""
Vorrei:

🛒 fare la spesa insieme la domenica

🍝 cucinare insieme

🛋️ passare le serate abbracciati sul divano

✈️ viaggiare insieme

🐶 avere un piccolo pelosetto

🏡 costruire una casa tutta nostra

❤️ e soprattutto, continuare a scegliere te ogni giorno.
""")

with st.expander("💌 C'è una cosa che voglio dirti..."):
    st.write("""
    Se sei arrivato fin qui, sappi che sceglierei te altre mille volte.
    In qualsiasi vita, in qualsiasi momento,
    spero di ritrovarti sempre.
    
    Buon compleanno amore mio ❤️
    """)
