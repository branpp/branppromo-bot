import requests
from telegram import Bot
import time

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

bot = Bot(token=TOKEN)

while True:

    url = "https://api.mercadolibre.com/sites/MLB/search?q=iphone"

    dados = requests.get(url).json()

    for produto in dados["results"][:5]:

        nome = produto["title"]
        preco = produto["price"]
        antigo = produto.get("original_price")

        if antigo and antigo > preco:

            desconto = ((antigo - preco) / antigo) * 100

            if desconto >= 20:

                mensagem = f"""
🔥 PROMOÇÃO DETECTADA

📱 {nome}

💸 DE: R$ {antigo}
✅ POR: R$ {preco}

🔥 {desconto:.0f}% OFF

🛒 {produto['permalink']}
"""

                bot.send_message(
                    chat_id=CHAT_ID,
                    text=mensagem
                )

    print("Verificando promoções...")

    time.sleep(3600)
