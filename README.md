Waifu AI Telegram Bot 💙🤖

Bot Telegram berbasis ASI1 Mini API, dikonfigurasi agar hanya pemilik bot yang bisa mengaksesnya.

🚀 Fitur

✅ Menjawab chat dengan gaya waifu.
✅ Menggunakan ASI1 Mini API untuk kecerdasan buatan.
✅ Hanya pemilik bot yang bisa menggunakannya.
✅ Bisa berjalan di OpenWRT, Replit, atau VPS.

🔧 Instalasi

1️⃣ Persyaratan

Sebelum menjalankan bot, pastikan Python 3 sudah terinstal.
Kemudian, instal dependensi dengan perintah:

pip install -r requirements.txt

2️⃣ Buat File .env (Opsional, untuk keamanan)

Buat file .env di folder utama dan isi dengan:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ASI1_API_KEY=your_asi1_api_key
OWNER_ID=your_telegram_user_id

Gantilah your_telegram_bot_token, your_asi1_api_key, dan your_telegram_user_id dengan milikmu sendiri.

3️⃣ Menjalankan Bot

Jalankan bot dengan perintah:

python bot.py

Jika ingin menjalankan di OpenWRT, gunakan:

nohup python3 bot.py &

Agar bot tetap berjalan di background.

🔑 Konfigurasi Keamanan

Bot ini hanya bisa diakses oleh pemiliknya. Jika orang lain mencoba menggunakannya, bot akan menolak perintah mereka.

Untuk mengubah Owner ID, edit bagian ini di bot.py:

OWNER_ID = 123456789  # Ganti dengan ID Telegram milikmu

@bot.message_handler(func=lambda message: message.chat.id == OWNER_ID)

📜 File Struktur

/bot-waifu-ai
│── bot.py              # Script utama bot
│── requirements.txt    # Library yang dibutuhkan
│── .env                # Token API & Bot (Opsional)
│── README.md           # Dokumentasi proyek

📌 Catatan

Pastikan API Key ASI1 valid!

Jika ingin bot online 24 jam, gunakan Replit, VPS, atau OpenWRT.

Jangan lupa backup token bot dan API key.


💙 Selamat mencoba! 🚀 
