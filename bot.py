import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYDZ9f0uMUE1vVo"
CHAT_ID = "@branppromo"

buscas = [
    "iphone", "samsung", "xiaomi", "motorola", "ssd", "monitor gamer",
    "cueca", "meia", "camisa", "camisa de time", "tenis nike",
    "air fryer", "perfume", "notebook", "mouse gamer", "fone bluetooth"
]

enviados = set()

def enviar_texto(texto):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": texto}
    )

def enviar_produto(produto):
    nome = produto.get("title", "Produto")
    preco = produto.get("price", "Consultar")
    link = produto.get("permalink", "")
    imagem = produto.get("thumbnail", "")

    texto = f"""
🛍️ ACHADINHO DO MERCADO LIVRE

📦 {nome}

💰 PREÇO: R$ {preco}

🛒 COMPRAR:
{link}
"""

    if imagem:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
            data={"chat_id": CHAT_ID, "photo": imagem, "caption": texto}
        )
    else:
        enviar_texto(texto)

enviar_texto("✅ Bot ligado! Procurando produtos...")

while True:
    try:
        pesquisa = random.choice(buscas)

        resposta = requests.get(
            "https://api.mercadolibre.com/sites/MLB/search",
            params={"q": pesquisa, "limit": 10}
        )

        dados = resposta.json()
        produtos = dados.get("results", [])

        if len(produtos) == 0:
            enviar_texto(f"⚠️ Nenhum produto encontrado para: {pesquisa}")
            time.sleep(10)
            continue

        random.shuffle(produtos)

        for produto in produtos[:3]:
            produto_id = produto.get("id")

            if produto_id in enviados:
                continue

            enviados.add(produto_id)
            enviar_produto(produto)

            time.sleep(10)

    except Exception as erro:
        enviar_texto(f"⚠️ Erro no bot: {erro}")

    time.sleep(10)
