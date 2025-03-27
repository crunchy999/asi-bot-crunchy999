__________________________________________
💙 Waifu AI Telegram Bot
__________________________________________
Bot Telegram berbasis ASI1 Mini API, dikonfigurasi agar hanya pemilik bot yang bisa mengaksesnya.
__________________________________________
✨ Fitur
__________________________________________
✔️ Menjawab chat dengan gaya waifu
✔️ Menggunakan ASI1 Mini API untuk kecerdasan buatan
✔️ Hanya pemilik bot yang bisa menggunakannya
✔️ Dapat berjalan di OpenWRT, Replit, atau VPS
__________________________________________
📦 Instalasi
__________________________________________
1️⃣ Persyaratan

Pastikan Python 3.8+ sudah terinstal.
Kemudian, instal dependensi dengan perintah:

pip install -r requirements.txt
__________________________________________
2️⃣ Konfigurasi
__________________________________________
Buat file .env di direktori utama dan isi dengan:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
ASI1_API_KEY=your_asi1_api_key
OWNER_ID=your_telegram_user_id

Penjelasan:

TELEGRAM_BOT_TOKEN → Token dari BotFather

ASI1_API_KEY → API key dari ASI1

OWNER_ID → ID Telegram pemilik bot (cek ID dengan @userinfobot)
__________________________________________
3️⃣ Menjalankan Bot
__________________________________________
Jalankan bot dengan perintah:

python bot.py

Jika ingin menjalankan di OpenWRT, gunakan:

nohup python3 bot.py &

(Agar bot tetap berjalan di background.)
__________________________________________
🔐 Konfigurasi Keamanan
__________________________________________
Bot ini hanya bisa digunakan oleh pemiliknya. Jika orang lain mencoba menggunakannya, bot akan menolak perintah mereka.

Untuk mengubah Owner ID, edit bagian ini di bot.py:

OWNER_ID = 123456789  # Ganti dengan ID Telegram kamu

@bot.message_handler(func=lambda message: message.chat.id == OWNER_ID)
__________________________________________
📂 Struktur Proyek
__________________________________________
/waifu-ai-bot
│── bot.py              # Script utama bot
│── requirements.txt    # Library yang dibutuhkan
│── .env                # Token API & Bot (Opsional)
│── README.md           # Dokumentasi proyek
__________________________________________
📝 TODO & Pengembangan
__________________________________________
✅ Menambahkan fitur mode waifu AI
✅ Membatasi akses hanya untuk pemilik
🔜 Menambahkan fitur voice chat untuk waifu AI
🔜 Membuat respons lebih interaktif
__________________________________________
📜 Lisensi
__________________________________________
Proyek ini dirilis di bawah lisensi MIT.
__________________________________________

💙 Selamat mencoba & semoga waifumu makin pintar! 🚀
