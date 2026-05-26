import requests

TOKEN = "8241926278:AAFSqaiWkRWONyK6q3wYbKb1AYdZOp7A3Ec"
CHAT_ID = "@branppromo"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

resposta = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "✅ TESTE: o bot está funcionando!"
})

print(resposta.text)
