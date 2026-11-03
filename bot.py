
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات من خوش آمدی 🌹")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    if message == "سلام":
        await update.message.reply_text("سلام عشخم! خوبی؟ 😊")

    elif message == "خوبی" or message == "مرسی. تو خوبی؟" or message=="ممنون.تو چطوری؟":
        await update.message.reply_text("به تو چه! تو چطوری؟ 😄")
    elif message == "مرسی خوبم":
        await update.message.reply_text("اوکی")
    else:
        await update.message.reply_text(message)
        
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
)

app.run_polling()



