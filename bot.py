import requests
from telegram import Bot
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYDZ9f0uMUE1vVo"
CHAT_ID = "@branppromo"

bot = Bot(token=TOKEN)

buscas = [
    "ssd",
    "memoria ram",
    "processador",
    "placa de video",
    "fone bluetooth",
    "headset gamer",
    "mouse gamer",
    "teclado mecanico",
    "monitor gamer",
    "cadeira gamer",
    "camisa",
    "camisa nike",
    "camisa adidas",
    "camisa de time",
    "cueca",
    "meia",
    "tenis nike",
    "tenis adidas",
    "smartphone",
    "iphone",
    "samsung",
    "xiaomi",
    "tv samsung",
    "notebook gamer",
    "ps5",
    "xbox",
    "controle ps5",
    "air fryer",
    "geladeira",
    "perfume",
    "relogio",
    "oculos",
    "moletom",
    "shorts",
    "bermuda",
    "kit roupa",
    "caixa de som",
    "echo dot",
    "alexa",
    "cadeira",
    "mesa gamer"
]

enviados = set()

def enviar_produto(produto):
    nome = produto["title"]
    preco = produto["price"]
    link = produto["permalink"]
    imagem = produto.get("thumbnail", "")

    antigo = produto.get("original_price")

    desconto_texto = ""

    if antigo and antigo > preco:
        desconto = int(((antigo - preco) / antigo) * 100)
        desconto_texto = f"\n🔥 Desconto: {desconto}% OFF"

    mensagem = f"""
🛒 {nome}

💰 Preço: R$ {preco}
{desconto_texto}

🔗 {link}
"""

    try:
        bot.send_photo(
            chat_id=CHAT_ID,
            photo=imagem,
            caption=mensagem
        )
    except:
        bot.send_message(
            chat_id=CHAT_ID,
            text=mensagem
        )

bot.send_message(
    chat_id=CHAT_ID,
    text="✅ Bot ligado! Procurando produtos no Mercado Livre..."
)

while True:
    try:
        pesquisa = random.choice(buscas)

        url = f"https://api.mercadolibre.com/sites/MLB/search?q={pesquisa}"

        resposta = requests.get(url)

        dados = resposta.json()

        produtos = dados.get("results", [])

        if not produtos:
            print(f"Nenhum produto encontrado para: {pesquisa}")
            time.sleep(10)
            continue

        random.shuffle(produtos)

        for produto in produtos[:5]:

            produto_id = produto["id"]

            if produto_id in enviados:
                continue

            enviados.add(produto_id)

            enviar_produto(produto)

            time.sleep(10)

    except Exception as erro:
        print("Erro:", erro)

    time.sleep(10)
