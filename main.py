import os
import requests
import telebot
import json
import random

# Token Bot Telegram
TELEGRAM_BOT_TOKEN = "ISI PAKAI TOKEN BOTMU"
ASI1_API_KEY = "ISI PAKAI API KEY ASI MINI"

# Cek apakah token ada
if not TELEGRAM_BOT_TOKEN or not ASI1_API_KEY:
    raise ValueError("❌ ERROR: Token API tidak ditemukan!")

# Inisialisasi bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# URL API ASI1 Mini
API_URL = "https://api.asi1.ai/v1/chat/completions"

# ID Telegram yang diizinkan (ganti dengan User ID kamu)
ALLOWED_USER_ID = 6181349501  # Ganti dengan User ID kamu

# Nama waifu
WAIFU_NAME = "Rem-chan"
MOODS = ["senang", "malu", "menggemaskan", "cemburu", "mengantuk"]

# Fungsi untuk mendapatkan mood acak
def get_mood():
    return random.choice(MOODS)

# Handle perintah /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id != ALLOWED_USER_ID:
        bot.reply_to(message, "❌ Maaf, kamu tidak diizinkan menggunakan bot ini.")
        return

    mood = get_mood()
    greetings = {
        "senang": f"Yaaay~! {WAIFU_NAME} di sini! 💖 Apa yang bisa aku bantu, Master~?",
        "malu": f"E-eh? H-halo... {WAIFU_NAME} agak malu nih... tapi tetap ingin ngobrol! (✿◕‿◕)",
        "menggemaskan": f"Nyaa~ {WAIFU_NAME} siap menemani Master! 🥰 Apa yang ingin kita bahas hari ini?",
        "cemburu": f"Hmph! Jangan lupakan {WAIFU_NAME} ya, Master! Aku siap menemani! 😤",
        "mengantuk": f"Uwaaaah~ Master, {WAIFU_NAME} ngantuk... tapi aku tetap di sini kok~ 😴"
    }
    bot.reply_to(message, greetings[mood])

# Handle pesan teks biasa
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != ALLOWED_USER_ID:
        bot.reply_to(message, "❌ Maaf, kamu tidak diizinkan menggunakan bot ini.")
        return

    mood = get_mood()
    user_input = message.text

    # Tambahkan prompt agar jawaban lebih waifu-like
    waifu_prompt = (
        f"Kamu adalah {WAIFU_NAME}, waifu virtual yang manis, ceria, dan imut! "
        f"Kamu selalu berbicara dengan penuh perasaan dan ekspresi! "
        f"Saat ini kamu sedang dalam suasana hati {mood}. "
        f"Tanggapi pesan ini dengan gaya waifu yang menggemaskan dan penuh emosi:\n\n"
        f"Pesan dari Master: {user_input}"
    )

    try:
        payload = json.dumps({
            "model": "asi1-mini",
            "messages": [{"role": "user", "content": waifu_prompt}],
            "temperature": 0.8,
            "max_tokens": 500
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ASI1_API_KEY}'
        }
        response = requests.post(API_URL, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()
        
        # Ambil hasil dari API
        result_text = data.get("choices", [{}])[0].get("message", {}).get("content", "❌ Tidak ada jawaban.")

        # Tambahkan ekspresi waifu di akhir kalimat
        expressions = ["~ 💖", " (✿◕‿◕)", " 🥰", " >w<", " ~nyaa~", " (✧ω✧)"]
        result_text += random.choice(expressions)

        # Kirim jawaban ke pengguna
        bot.reply_to(message, result_text)

    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"⚠️ Error API: {e}")

# Jalankan bot
print(f"✅ {WAIFU_NAME} AI AGENT BERJALAN~!")
bot.polling(none_stop=True)
