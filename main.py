from telethon import TelegramClient, events

# --- Gerekli Bilgiler ---
api_id = int("24709161")  # API_ID
api_hash = "545957fb3651eb9987e97e2fe40bf586"  # API_HASH
phone_number = "+90XXXXXXXXXX"  # Telefon numaranı buraya yaz
target_username = "hedef_kullanici_adi"  # Takip etmek istediğin kişi (@kullanciadi)

# --- Client Başlat ---
client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage)
async def catch_target_user(event):
    sender = await event.get_sender()
    if sender and sender.username == target_username:
        message = f"[{sender.first_name}] {event.text}"
        await client.send_message("me", message)  # "me" Saved Messages anlamına gelir

client.start(phone_number)
print("Userbot çalışıyor... Hedef kullanıcıdan mesaj bekleniyor.")
client.run_until_disconnected()
