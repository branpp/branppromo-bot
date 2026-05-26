import requests
import time

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": texto})

while True:
    try:
        url = "https://api.mercadolibre.com/sites/MLB/search?q=iphone"

        dados = requests.get(url).json()

        for produto in dados["results"][:10]:

            nome = produto["title"]
            preco = produto["price"]
            antigo = produto.get("original_price")
            link = produto["permalink"]

            if antigo and antigo > preco:

                desconto = ((antigo - preco) / antigo) * 100

                if desconto >= 20:

                    mensagem = f"""
🔥 PROMOÇÃO DETECTADA

📱 {nome}

💸 DE: R$ {antigo}
✅ POR: R$ {preco}

🔥 {desconto:.0f}% OFF

🛒 {link}
"""

                    enviar_mensagem(mensagem)

        print("Verificando promoções...")

    except Exception as erro:
        print("Erro:", erro)

    time.sleep(3600)
