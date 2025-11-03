from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")


main_menu = [
    ["ℹ️ О боте", "📞 Контакты"],
    ["📰 Новости", "❌ Закрыть меню"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_firstname = update.effective_user.first_name
    keyboard = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text(
        f"Привет, {user_firstname}! 👋\nЯ бот, запущенный на Render.\nВыбери нужный пункт из меню:",
        reply_markup=keyboard
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "ℹ️ О боте":
        await update.message.reply_text("Я демонстрационный Telegram-бот, размещённый на Render 🚀")
    elif text == "📞 Контакты":
        await update.message.reply_text("Свяжись с нами: support@example.com")
    elif text == "📰 Новости":
        await update.message.reply_text("Пока новостей нет 😅")
    elif text == "❌ Закрыть меню":
        await update.message.reply_text("Меню скрыто 👋", reply_markup=None)
    else:
        await update.message.reply_text("Я не понял 😅 — воспользуйся меню ниже 👇")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("menu", start)) 
    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
