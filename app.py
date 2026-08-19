# ============================================================
# TESTE DO STREAMLIT
# ============================================================

import streamlit as st

st.set_page_config(
    page_title="Conselho de IAs",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Conselho de IAs")

st.subheader(
    "Sistema multiagente para análise e tomada de decisão"
)

st.success("O Streamlit está funcionando!")

st.write("Agora vamos testar o carregamento do agente.")