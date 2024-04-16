import logging
from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,  MessageHandler, filters
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
import os
from app import chai
load_dotenv()
TOKEN = os.getenv('apitele')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = chai(user_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sedang memproses pesanmu...")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = update.effective_user.id
    logging.info(f"Pesan dari pengguna dengan ID {user_id}: {user_message}")

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    # message_handler = MessageHandler()
    application.add_handler(start_handler)
    # Uncomment the line below to add the MessageHandler for handling messages
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    # MessageHandler(filters.TEXT, handle_message)
    
    application.run_polling()