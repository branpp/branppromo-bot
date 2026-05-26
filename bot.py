import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

buscas = [

    # CELULARES
    "iphone", "iphone 15", "iphone 16",
    "samsung", "xiaomi", "motorola",

    # INFORMÁTICA
    "notebook", "pc gamer", "ssd",
    "placa de video", "monitor gamer",
    "memoria ram", "processador ryzen",

    # PERIFÉRICOS
    "mouse gamer", "teclado mecanico",
    "headset gamer",

    # CONSOLES
    "ps5", "xbox", "nintendo switch",

    # TV E ELETRÔNICOS
    "smart tv", "jbl", "airpods",
    "apple watch", "tablet",

    # CASA
    "air fryer", "cafeteira",
    "microondas", "geladeira",

    # ROUPAS
    "camisa nike", "camisa adidas",
    "camiseta", "bermuda",
    "calca jeans", "moletom",

    # FUTEBOL
    "camisa de time", "camisa flamengo",
    "camisa corinthians", "camisa bahia",

    # ROUPAS ÍNTIMAS
    "cueca", "cueca boxer",
    "meia", "kit meia",

    # TÊNIS
    "tenis nike", "tenis adidas",
    "tenis mizuno",

    # PERFUMES
    "perfume masculino",
    "perfume feminino",
    "malbec",

    # ACESSÓRIOS
    "relogio masculino",
    "mochila",

    # ALEATÓRIOS
    "drone", "camera",
    "bicicleta", "lego",
    "funko pop"
]

def enviar_texto(texto):

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": texto
        }
    )

def enviar_produto(nome, preco, antigo, link, imagem):

    if antigo and antigo > preco:

        desconto = ((antigo - preco) / antigo) * 100

        texto = f"""
🔥 PROMOÇÃO ENCONTRADA

📦 {nome}

💸 DE: R$ {antigo}
✅ POR: R$ {preco}

🔥 {desconto:.0f}% OFF

🛒 COMPRAR:
{link}
"""

    else:

        texto = f"""
🛍️ ACHADINHO DO MERCADO LIVRE

📦 {nome}

💰 PREÇO: R$ {preco}

🛒 COMPRAR:
{link}
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={
            "chat_id": CHAT_ID,
            "photo": imagem,
            "caption": texto
        }
    )

enviar_texto("✅ Bot ligado! Procurando produtos...")

while True:

    try:

        pesquisa = random.choice(buscas)

        url = f"https://api.mercadolibre.com/sites/MLB/search?q={pesquisa}&limit=10"

        resposta = requests.get(url)

        dados = resposta.json()

        produtos = dados["results"]

        for produto in produtos[:3]:

            nome = produto.get("title", "Produto")
            preco = produto.get("price", "0")
            antigo = produto.get("original_price")
            link = produto.get("permalink", "")
            imagem = produto.get("thumbnail", "")

            enviar_produto(
                nome,
                preco,
                antigo,
                link,
                imagem
            )

            time.sleep(15)

    except Exception as erro:

        enviar_texto(f"⚠️ Erro: {erro}")

    time.sleep(10)
