import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

buscas = ["iphone", "samsung", "xiaomi", "cueca", "meia", "camisa", "air fryer", "ssd"]

def enviar(texto):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": texto}
    )

enviar("✅ Bot reiniciado! Testando Mercado Livre...")

while True:
    try:
        pesquisa = random.choice(buscas)

        resposta = requests.get(
            "https://api.mercadolibre.com/sites/MLB/search",
            params={"q": pesquisa, "limit": 1},
            timeout=15
        )

        enviar(f"🔎 Buscando: {pesquisa}\nStatus API: {resposta.status_code}")

        dados = resposta.json()
        produtos = dados.get("results", [])

        if not produtos:
            enviar("⚠️ A API respondeu, mas não trouxe produtos.")
        else:
            produto = produtos[0]

            nome = produto.get("title", "Produto")
            preco = produto.get("price", "Consultar")
            link = produto.get("permalink", "")

            enviar(f"""
🛍️ ACHADINHO DO MERCADO LIVRE

📦 {nome}

💰 PREÇO: R$ {preco}

🛒 COMPRAR:
{link}
""")

    except Exception as erro:
        enviar(f"⚠️ ERRO REAL: {erro}")

    time.sleep(20)
