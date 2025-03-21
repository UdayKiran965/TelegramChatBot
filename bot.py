import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import cohere

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Cohere API
cohere_client = cohere.Client('raFq7VA9yIRDcglQKnUhyz7pANqJxjrNO0c01HMU')

# Define start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I am your Uday's  AI-powered bot. How can I Assists you 😊!")

# Function to process messages and interact with Cohere AI
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Generate response using Cohere
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=user_message,
        max_tokens=1500
    )

    # Send the Cohere response back to the user
    await update.message.reply_text(response.generations[0].text.strip())

# Error handler
async def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Telegram Bot Token
    application = Application.builder().token("7579589110:AAEgu9BK3uH0h5Rh2jKJZvbOiDgtUIAG3ao").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
