from telegram.ext import ApplicationBuilder, CommandHandler
import requests

TOKEN = "8542516479:AAFkqdUz97KV2Fyh60PiYaBMhpEkNj-scec"

async def namaz(update, context):
    city = "Dushanbe"
    country = "Tajikistan"

    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    data = requests.get(url).json()
    t = data["data"]["timings"]

    text = (
        "🕌 Время намаза\n\n"
        f"Фаджр: {t['Fajr']}\n"
        f"Зухр: {t['Dhuhr']}\n"
        f"Аср: {t['Asr']}\n"
        f"Магриб: {t['Maghrib']}\n"
        f"Иша: {t['Isha']}"
    )

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("namaz", namaz))
app.run_polling()