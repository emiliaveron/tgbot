import logging
import telegram as tg
import telegram.ext as tgx

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def name(update: tg.Update, context: tg.CallbackContext):
    query = update.callback_query

    query.answer()
    
    keyboard = [[
        tg.InlineKeyboardButton("Go back ↩️", callback_data='back')]]
    
    return NAME

async def start(update: tg.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to your radfem helper bot!")
    
    keyboard = [[
        tg.InlineKeyboardButton("Why the name?", callback_data='name')],
        [tg.InlineKeyboardButton("What's the difference?", callback_data='diff')],
        [tg.InlineKeyboardButton("The patriarchy", callback_data='patriarchy'),
        tg.InlineKeyboardButton("Gender socialization", callback_data='prost')
        ]]
    
    reply_markup = tg.InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('This bot will answer all the questions about radical feminist theory that you could have. Just choose a category below:', reply_markup=reply_markup)

async def echo(update: tg.Update, context: tgx.ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry!! As of now, the bot only understands the choices in the menu! :()")

def main():
    updater = tgx.ApplicationBuilder().token('7154497401:AAGz2IX4-qG9r_DwdQdMbtHFfgsNDz2zTCo').build()
    
    updater.add_handler(tgx.CommandHandler('start', start))
    # updater.add_handler(tgx.CallbackQueryHandler(button))
    updater.add_handler(tgx.CommandHandler('echo', echo))

     conv_handler = tgx.ConversationHandler(
        entry_points=[tgx.CommandHandler("start", start)],
        states={
            START_ROUTES: [
                tgx.CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                tgx.CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                tgx.CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
                tgx.CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
            ],
            END_ROUTES: [
                tgx.CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                tgx.CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )


    updater.run_polling()


if __name__ == '__main__':
    main()