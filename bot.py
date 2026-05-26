import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

buscas = [

    # CELULARES
    "iphone", "iphone 15", "iphone 16", "iphone barato",
    "samsung", "galaxy s24", "xiaomi", "redmi note",
    "motorola", "poco x6", "smartphone",

    # INFORMÁTICA
    "notebook", "notebook gamer", "pc gamer",
    "placa de video", "rx 6600", "rtx 4060",
    "ssd", "ssd nvme", "memoria ram",
    "processador ryzen", "monitor gamer",
    "cadeira gamer", "mesa gamer",

    # PERIFÉRICOS
    "teclado mecanico", "mouse gamer", "headset gamer",
    "controle xbox", "controle ps5",
    "webcam", "microfone gamer",

    # CONSOLES
    "ps5", "playstation 5", "xbox series s",
    "xbox series x", "nintendo switch",

    # TV E ELETRÔNICOS
    "smart tv", "tv samsung", "tv lg",
    "caixa jbl", "jbl", "airpods",
    "apple watch", "smartwatch",
    "tablet", "ipad", "kindle",

    # CASA
    "air fryer", "cafeteira", "microondas",
    "geladeira", "fogao", "lavadora",
    "aspirador robo", "ventilador",

    # ROUPAS
    "camisa nike", "camisa adidas",
    "camisa masculina", "camisa feminina",
    "camisa oversized", "camiseta basica",
    "bermuda masculina", "calca jeans",
    "moletom", "jaqueta masculina",

    # FUTEBOL
    "camisa de time", "camisa flamengo",
    "camisa corinthians", "camisa palmeiras",
    "camisa bahia", "camisa real madrid",
    "camisa barcelona", "camisa selecao brasileira",

    # ROUPAS ÍNTIMAS
    "cueca", "cueca boxer", "kit cueca",
    "meia", "kit meia", "meia nike",
    "calcinha", "lingerie",

    # TÊNIS
    "tenis nike", "tenis adidas",
    "tenis mizuno", "tenis olympikus",
    "tenis corrida", "tenis casual",

    # PERFUMES
    "perfume importado", "perfume masculino",
    "perfume feminino", "212 vip",
    "malbec", "kaiak",

    # ACESSÓRIOS
    "relogio masculino", "oculos de sol",
    "corrente prata", "pulseira masculina",
    "mochila", "bolsa feminina",

    # ALEATÓRIOS
    "drone", "camera", "gopro",
    "bicicleta", "patinete eletrico",
    "brinquedo", "lego", "funko pop",
    "pokemon", "minecraft", "livro",
    "manga", "hq", "action figure"
]

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

    url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    requests.post(url_telegram, data={
        "chat_id": CHAT_ID,
        "photo": imagem,
        "caption": texto
    })

while True:

    try:

        pesquisa = random.choice(buscas)

        url = f"https://api.mercadolibre.com/sites/MLB/search?q={pesquisa}"

        dados = requests.get(url).json()

        produtos = dados["results"][:3]

        for produto in produtos:

            nome = produto["title"]
            preco = produto["price"]
            antigo = produto.get("original_price")
            link = produto["permalink"]
            imagem = produto["thumbnail"]

            enviar_produto(nome, preco, antigo, link, imagem)

            time.sleep(20)

    except Exception as erro:
        print("Erro:", erro)

    time.sleep(20)
