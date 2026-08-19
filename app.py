# ============================================================
# CONSELHO DE IAs
# INTERFACE WEB COM STREAMLIT
# ============================================================

import streamlit as st

from main import agente_estrategista


# ------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ------------------------------------------------------------

st.set_page_config(
    page_title="Conselho de IAs",
    page_icon="🧠",
    layout="wide"
)


# ------------------------------------------------------------
# TÍTULO
# ------------------------------------------------------------

st.title("🧠 Conselho de IAs")

st.subheader(
    "Sistema multiagente para análise e tomada de decisão"
)


# ------------------------------------------------------------
# CAMPO DE PERGUNTA
# ------------------------------------------------------------

pergunta = st.text_area(
    "Digite sua pergunta:",
    height=150,
    placeholder="Exemplo: Devo aprender Python ou SQL primeiro?"
)


# ------------------------------------------------------------
# BOTÃO
# ------------------------------------------------------------

if st.button("🚀 Consultar Conselho"):

    if not pergunta.strip():

        st.warning(
            "Digite uma pergunta antes de consultar."
        )

    else:

        # ----------------------------------------------------
        # CONSULTAR O ESTRATEGISTA
        # ----------------------------------------------------

        with st.spinner(
            "🧠 O Estrategista está analisando..."
        ):

            resposta = agente_estrategista(pergunta)


        # ----------------------------------------------------
        # MOSTRAR RESULTADO
        # ----------------------------------------------------

        st.divider()

        st.header(
            "🧠 Análise do Estrategista"
        )

        st.write(resposta)