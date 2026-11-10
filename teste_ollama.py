# ============================================================
# TESTE DE INTEGRAÇÃO PYTHON + OLLAMA
# ============================================================

import requests


# ------------------------------------------------------------
# 1. ENDEREÇO DA API DO OLLAMA
# ------------------------------------------------------------

url = "http://localhost:11434/api/generate"


# ------------------------------------------------------------
# 2. PERGUNTA PARA O QWEN
# ------------------------------------------------------------

dados = {
    "model": "qwen3:8b",
    "prompt": "Explique em uma frase o que é pensamento crítico.",
    "stream": False
}


# ------------------------------------------------------------
# 3. ENVIAR PERGUNTA
# ------------------------------------------------------------

resposta = requests.post(
    url,
    json=dados
)


# ------------------------------------------------------------
# 4. VERIFICAR RESULTADO
# ------------------------------------------------------------

if resposta.status_code == 200:

    resultado = resposta.json()

    print()
    print("=" * 60)
    print("RESPOSTA DO QWEN3")
    print("=" * 60)
    print()

    print(resultado["response"])

    print()
    print("=" * 60)

else:

    print("ERRO AO CONSULTAR O OLLAMA")
    print("Código:", resposta.status_code)
    print(resposta.text)