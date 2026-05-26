import requests
from bs4 import BeautifulSoup
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

enviar("✅ Bot scraping ligado!")

while True:

    try:

        pesquisa = random.choice(buscas)

        url = f"https://lista.mercadolivre.com.br/{pesquisa}"

        resposta = requests.get(url, headers=headers)

        soup = BeautifulSoup(resposta.text, "html.parser")

        links = soup.select("a.poly-component__title")

        if not links:
            enviar(f"⚠️ Nenhum produto encontrado para: {pesquisa}")
            time.sleep(10)
            continue

        produto = random.choice(links)

        nome = produto.text.strip()
        link = produto.get("href")

        if link in enviados:
            continue

        enviados.add(link)

        mensagem = f"""
🛍️ ACHADINHO DO MERCADO LIVRE

📦 {nome}

🛒 COMPRAR:
{link}
"""

        enviar(mensagem)

    except Exception as erro:

        enviar(f"⚠️ ERRO: {erro}")

    time.sleep(10)
