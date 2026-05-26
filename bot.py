import requests
import time
import random

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

buscas = [
    "iphone", "samsung", "xiaomi", "motorola",
    "notebook", "notebook gamer", "pc gamer",
    "placa de video", "rtx 4060", "ssd", "memoria ram",
    "processador ryzen", "monitor gamer", "teclado mecanico",
    "mouse gamer", "headset gamer", "cadeira gamer",
    "ps5", "xbox", "nintendo switch",
    "smart tv", "tv samsung", "tv lg",
    "air fryer", "cafeteira", "microondas",
    "apple watch", "airpods", "caixa jbl",
    "perfume", "tenis nike", "tenis adidas",
    "camisa futebol", "kit gamer",
    "drone", "camera", "gopro",
    "bicicleta", "patinete eletrico",
    "tablet", "ipad"
]

def enviar_promocao(nome, preco, antigo, desconto, link, imagem):
    texto = f"""
🔥 PROMOÇÃO ENCONTRADA

📦 {nome}

💸 DE: R$ {antigo}
✅ POR: R$ {preco}

🔥 DESCONTO: {desconto:.0f}% OFF

🛒 COMPRAR:
{link}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "photo": imagem,
        "caption": texto
    })

while True:
    try:
        pesquisa = random.choice(buscas)
        url = f"https://api.mercadolibre.com/sites/MLB/search?q={pesquisa}"

        dados = requests.get(url).json()

        for produto in dados["results"][:10]:
            nome = produto["title"]
            preco = produto["price"]
            antigo = produto.get("original_price")
            link = produto["permalink"]
            imagem = produto["thumbnail"]

            if antigo and antigo > preco:
                desconto = ((antigo - preco) / antigo) * 100

                if desconto >= 10:
                    enviar_promocao(nome, preco, antigo, desconto, link, imagem)
                    time.sleep(15)

    except Exception as erro:
        print("Erro:", erro)

    time.sleep(1800)
