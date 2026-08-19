# ============================================================
# CONSELHO DE IAs
# VERSÃO 1.0
# Primeiro agente utilizando a Gemini API
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ------------------------------------------------------------

import os
# A biblioteca "os" permite acessar informações
# do sistema operacional.
#
# Vamos utilizá-la para pegar nossa API Key.


from dotenv import load_dotenv
# "load_dotenv" permite que o Python leia
# as variáveis armazenadas no arquivo .env.


from google import genai
# Importamos o SDK oficial da Google para a Gemini API.
#
# É através dele que nosso Python vai conversar
# com o Gemini.



# ------------------------------------------------------------
# 2. CARREGAR O ARQUIVO .ENV
# ------------------------------------------------------------

load_dotenv()

# O Streamlit Cloud utiliza st.secrets.
# No computador local, utilizamos o arquivo .env.

try:
    import streamlit as st
except ImportError:
    st = None



# ------------------------------------------------------------
# 3. PEGAR A API KEY DO GEMINI
# ------------------------------------------------------------

api_key = os.getenv("GEMINI_API_KEY")

# Se não encontrou no .env, tenta buscar
# nos Secrets do Streamlit Cloud.

if not api_key and st is not None:

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

    except Exception:
        api_key = None



# ------------------------------------------------------------
# 4. VERIFICAR SE A API KEY EXISTE
# ------------------------------------------------------------

if not api_key:

    print("ERRO: API Key do Gemini não encontrada.")
    print("Verifique o arquivo .env ou os Secrets do Streamlit.")



# ------------------------------------------------------------
# 5. CRIAR O CLIENTE DO GEMINI
# ------------------------------------------------------------

client = None

if api_key:
    client = genai.Client(
        api_key=api_key
    )

# Aqui criamos o nosso cliente.
#
# Pense nele como uma ponte:
#
# Python
#   ↓
# client
#   ↓
# Gemini API
#   ↓
# Modelo Gemini



# ------------------------------------------------------------
# 6. APRESENTAÇÃO DO PROGRAMA
# ------------------------------------------------------------

print("=" * 60)
print("              CONSELHO DE IAs")
print("=" * 60)

print()

print("Primeiro agente conectado ao Gemini.")

print()



# ------------------------------------------------------------
# 7. FUNÇÃO PARA CONSULTAR O GEMINI
# ------------------------------------------------------------

def consultar_gemini(pergunta):
    """
    Envia uma pergunta para o Gemini
    e devolve a resposta.
    """

    if client is None:
        raise ValueError(
            "API Key do Gemini não configurada."
        )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=pergunta
    )

    return response.text


# ============================================================
# 8. AGENTE ESTRATEGISTA
# ============================================================

def agente_estrategista(pergunta):
    """
    Primeiro membro do Conselho.

    Sua função é analisar o problema,
    encontrar alternativas e propor
    uma solução.
    """

    prompt = f"""
Você é o ESTRATEGISTA do Conselho de IAs.

Sua função é analisar problemas de forma profunda
e estruturada.

Para cada problema:

1. Identifique o problema principal.
2. Separe fatos de suposições.
3. Liste possíveis alternativas.
4. Analise vantagens e desvantagens.
5. Identifique riscos.
6. Recomende a melhor alternativa.
7. Explique por que ela é a melhor.

Não tente agradar o usuário.
Priorize lógica, evidências e coerência.

Problema apresentado pelo usuário:

{pergunta}
"""

    return consultar_gemini(prompt)


# ------------------------------------------------------------
# 9. EXECUÇÃO DO PROGRAMA PELO TERMINAL
# ------------------------------------------------------------

if __name__ == "__main__":

    # Só executa esta parte quando rodarmos:
    #
    # python main.py
    #
    # Quando o Streamlit importar o arquivo,
    # esta parte NÃO será executada.

    pergunta = input("Digite sua pergunta: ")


    # --------------------------------------------------------
    # 10. CONSULTAR O ESTRATEGISTA
    # --------------------------------------------------------

    resposta = agente_estrategista(pergunta)


    # --------------------------------------------------------
    # 11. MOSTRAR A RESPOSTA
    # --------------------------------------------------------

    print()

    print("-" * 60)

    print("ANÁLISE DO ESTRATEGISTA")

    print("-" * 60)

    print()

    print(resposta)

    print()

    print("-" * 60)