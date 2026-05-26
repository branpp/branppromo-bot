import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

buscas = ["iphone", "samsung", "xiaomi", "cueca", "meia", "camisa de time", "air fryer", "ssd", "monitor gamer"]

def enviar_texto(texto):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": texto
    })

def enviar_produto(nome, preco, link, imagem):
    texto = f"""
🛍️ ACHADINHO DO MERCADO LIVRE

📦 {nome}

💰 PREÇO: R$ {preco}

🛒 COMPRAR:
{link}
"""
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data={
        "chat_id": CHAT_ID,
        "photo": imagem,
        "caption": texto
    })

enviar_texto("✅ Bot ligado! Procurando produtos no Mercado Livre...")

while True:
    try:
        pesquisa = random.choice(buscas)
        url = f"https://api.mercadolibre.com/sites/MLB/search?q={pesquisa}"

        dados = requests.get(url).json()
        produtos = dados.get("results", [])[:3]

        if not produtos:
            enviar_texto(f"⚠️ Nenhum produto encontrado para: {pesquisa}")

        for produto in produtos:
            enviar_produto(
                produto.get("title", "Produto"),
                produto.get("price", "Consultar"),
                produto.get("permalink", ""),
                produto.get("thumbnail", "")
            )
            time.sleep(10)

    except Exception as erro:
        enviar_texto(f"⚠️ Erro no bot: {erro}")

    time.sleep(60)
