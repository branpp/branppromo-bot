import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

buscas = [
    "iphone",
    "samsung",
    "xiaomi",
    "ssd",
    "air fryer",
    "camisa",
    "camisa de time",
    "meia",
    "cueca",
    "tenis nike",
    "monitor gamer",
    "mouse gamer",
    "headset gamer",
    "notebook",
    "jbl"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

enviados = set()

def enviar(texto):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": texto
        }
    )

def enviar_produto(produto):
    nome = produto.get("title", "Produto")
    preco = produto.get("price", "Consultar")
    link = produto.get("permalink", "")

    texto = f"""
🛍️ ACHADINHO DO MERCADO LIVRE

📦 {nome}

💰 PREÇO: R$ {preco}

🛒 COMPRAR:
{link}
"""

    enviar(texto)

enviar("✅ Bot ligado com correção 403!")

while True:

    try:

        pesquisa = random.choice(buscas)

        resposta = requests.get(
            "https://api.mercadolibre.com/sites/MLB/search",
            params={
                "q": pesquisa,
                "limit": 5
            },
            headers=headers,
            timeout=20
        )

        enviar(f"🔎 Buscando: {pesquisa}")

        dados = resposta.json()

        produtos = dados.get("results", [])

        if not produtos:
            enviar("⚠️ Nenhum produto encontrado.")
            time.sleep(10)
            continue

        for produto in produtos:

            produto_id = produto.get("id")

            if produto_id in enviados:
                continue

            enviados.add(produto_id)

            enviar_produto(produto)

            time.sleep(10)

    except Exception as erro:

        enviar(f"⚠️ ERRO: {erro}")

    time.sleep(10)
