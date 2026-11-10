# ============================================================
# CONSELHO DE IAs
# VERSÃO 1.1
# Estrategista utilizando Gemini + Crítico utilizando Ollama
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ------------------------------------------------------------

import os
import requests

from dotenv import load_dotenv
from google import genai


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


# ------------------------------------------------------------
# 6. APRESENTAÇÃO DO PROGRAMA
# ------------------------------------------------------------

print("=" * 60)
print("              CONSELHO DE IAs")
print("=" * 60)

print()

print("Estrategista: Gemini")
print("Crítico: Qwen3 8B via Ollama")

print()


# ============================================================
# 7. FUNÇÃO PARA CONSULTAR O GEMINI
# ============================================================

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
# 8. FUNÇÃO PARA CONSULTAR O OLLAMA
# ============================================================

def consultar_ollama(prompt):
    """
    Envia uma solicitação para o Ollama
    e devolve a resposta do modelo local.
    """

    url = "http://localhost:11434/api/generate"

    dados = {
        "model": "qwen3:8b",
        "prompt": prompt,
        "stream": False
    }

    resposta = requests.post(
        url,
        json=dados
    )

    if resposta.status_code != 200:

        raise ValueError(
            f"Erro ao consultar o Ollama: "
            f"{resposta.status_code} - {resposta.text}"
        )

    resultado = resposta.json()

    return resultado["response"]


# ============================================================
# 9. AGENTE ESTRATEGISTA
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

Priorize:

- lógica;
- evidências;
- coerência;
- análise de riscos;
- comparação entre alternativas.

Problema apresentado pelo usuário:

{pergunta}
"""

    return consultar_gemini(prompt)


# ============================================================
# 10. AGENTE CRÍTICO
# ============================================================

def agente_critico(analise):
    """
    Segundo membro do Conselho.

    Sua função é auditar a análise produzida
    pelo Estrategista, procurando falhas,
    lacunas, vieses e informações insuficientes.
    """

    prompt = f"""
Você é o CRÍTICO do Conselho de IAs.

Outro agente, chamado ESTRATEGISTA, produziu
uma análise sobre um problema apresentado pelo usuário.

Sua função NÃO é simplesmente produzir uma nova resposta.

Sua função é AUDITAR a análise recebida.

Analise cuidadosamente:

1. O que o Estrategista fez corretamente.
2. O que ele deixou de considerar.
3. Quais afirmações são vagas ou não possuem evidências.
4. Quais premissas podem estar incorretas.
5. Quais riscos foram ignorados.
6. Quais possíveis vieses existem.
7. Quais informações adicionais deveriam ser obtidas.
8. Dê uma nota de 0 a 10 para a qualidade da análise.

Seja rigoroso e independente.

Não concorde com o Estrategista apenas para
produzir uma resposta agradável.

Não tente substituir completamente a análise.

Seu objetivo é encontrar possíveis problemas
na análise apresentada.

ANÁLISE DO ESTRATEGISTA:

{analise}
"""

    return consultar_ollama(prompt)


# ============================================================
# 11. EXECUÇÃO DO PROGRAMA PELO TERMINAL
# ============================================================

if __name__ == "__main__":

    # Só executa esta parte quando rodarmos:
    #
    # python main.py
    #
    # Quando o Streamlit importar o arquivo,
    # esta parte NÃO será executada.


    # --------------------------------------------------------
    # 12. RECEBER PERGUNTA DO USUÁRIO
    # --------------------------------------------------------

    pergunta = input(
        "Digite sua pergunta: "
    )


    # --------------------------------------------------------
    # 13. CONSULTAR O ESTRATEGISTA
    # --------------------------------------------------------

    print()
    print("🧠 Consultando o Estrategista...")

    resposta = agente_estrategista(
        pergunta
    )


    # --------------------------------------------------------
    # 14. CONSULTAR O CRÍTICO
    # --------------------------------------------------------

    print()
    print("🦙 Consultando o Crítico...")

    critica = agente_critico(
        resposta
    )


    # --------------------------------------------------------
    # 15. MOSTRAR ANÁLISE DO ESTRATEGISTA
    # --------------------------------------------------------

    print()

    print("-" * 60)

    print("ANÁLISE DO ESTRATEGISTA")

    print("-" * 60)

    print()

    print(resposta)


    # --------------------------------------------------------
    # 16. MOSTRAR ANÁLISE DO CRÍTICO
    # --------------------------------------------------------

    print()

    print("-" * 60)

    print("ANÁLISE DO CRÍTICO")

    print("-" * 60)

    print()

    print(critica)

    print()

    print("-" * 60)

    print("FIM DA ANÁLISE")
    print("-" * 60)