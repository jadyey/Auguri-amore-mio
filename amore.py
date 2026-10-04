import streamlit as st
st.markdown("""
<style>
    .stApp {
        background-color: #fff0f5;
    }

    h1 {
        color: #d63384;
        text-align: center;
    }

    h3 {
        color: #c2185b;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Buon Compleanno tato 🩷", page_icon= "🎂")
st.title("Tanti auguri amore mio 💕  🎂🎂")
st.audio("Paramore_StillIntoYou.mp3")
st.image("yahya.jpeg", caption="Noi due <3", width=500)
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
with st.expander("💌 C'è una cosa che voglio dirti..."):
    st.write("""
    Se sei arrivato fin qui, sappi che...
    
    sceglierei te altre mille volte.
    
    Buon compleanno amore mio ❤️
    """)
