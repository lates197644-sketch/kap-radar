import os
import time
import requests

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def telegram_gonder(mesaj):
    if not BOT_TOKEN or not CHAT_ID:
        print("Telegram ayarlari eksik.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    cevap = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": mesaj
        },
        timeout=20
    )

    cevap.raise_for_status()


print("KAP Radar baslatiliyor...")

telegram_gonder(
    "🚀 KAP RADAR AKTİF\n\n"
    "Telegram bağlantısı başarıyla kuruldu.\n"
    "KAP bildirim sistemi çalışmaya hazır."
)

while True:
    print("KAP Radar çalışıyor...")
    time.sleep(60)
