import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to your radfem helper bot!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="This bot will answer all the questions about radical feminist theory that you could have. Just choose a category below:")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry!! As of now, the bot only understands the choices in the menu! :()")



if __name__ == '__main__':
    application = ApplicationBuilder().token('7154497401:AAGz2IX4-qG9r_DwdQdMbtHFfgsNDz2zTCo').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()