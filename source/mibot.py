import logging
from telegram.ext import Updater, CommandHandler
from conf import TOKEN


LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_DATE = '%d/%m/%Y %H:%M:%S'
logging.addLevelName(logging.ERROR, '\033[1;41mERROR\033[1;0m')
logging.addLevelName(logging.DEBUG, '\x1b[33mDEBUG\033[1;0m')
logging.addLevelName(logging.INFO, '\x1b[32mINFO\033[1;0m')
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=LOG_DATE)
log = logging.getLogger(__name__)


def start(update, context):
    bot = context.bot
    chat_id = update.effective_chat.id
    user = update.message.from_user
    text = f'Hola {user.username},\n\n soy botsque'

    bot.send_message(chat_id=chat_id, text=text)
    return


def ayuda(update, context):
    bot = context.bot
    chat_id = update.effective_chat.id
    user = update.message.from_user
    text = '/ayuda Conoce todos los comandos para visitar el botsque'

    bot.send_message(chat_id=chat_id, text=text)
    return



def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('ayuda', ayuda))

    updater.start_polling()
    updater.idle()
    return


if __name__ == '__main__':
    main()

