from database import DataBase
from telegram.ext import Updater, CommandHandler,  CallbackQueryHandler, MessageHandler, Filters
from configparser import ConfigParser
import command_manager
import btn_callback_handler


def main():
    config = ConfigParser()
    config.read("files/config.ini")

    token = config["Telegram"]["token"]
    updater = Updater(token)
    db = DataBase()
    db.create_tables()
    db.close()
    dispatchers(updater)

    updater.start_polling()
    updater.idle()


def dispatchers(updater):
    updater.dispatcher.add_handler(CommandHandler('start', command_manager.start))
    updater.dispatcher.add_handler(CommandHandler('reload_posts', command_manager.reload_posts))
    updater.dispatcher.add_handler(CommandHandler('summary', command_manager.summary))
    
    updater.dispatcher.add_handler(MessageHandler(Filters.text | Filters.command | Filters.photo | Filters.audio | Filters.document, command_manager.invalid_cmd))
    updater.dispatcher.add_handler(CallbackQueryHandler( btn_callback_handler.btn_response))


if __name__ == "__main__":
    main()