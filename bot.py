import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

message = "✅ GitHub Bot Connected Successfully!\n\nBench Sales Job Bot is Ready 🚀"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHANNEL_ID,
        "text": message
    }
)

print(response.text)
