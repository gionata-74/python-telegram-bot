from user import User
from database import DataBase, UserDatabase
from telegram.ext import CallbackContext
from telegram import Update

import console
import tools
import channel_scraper


def start(update: Update, context: CallbackContext) -> None:

    udb = UserDatabase()
    udb.create_table()
    chat_id = update.message.chat_id
    t = update.message.date
    user_name = str(update.effective_user.username)
    full_name = str(update.effective_user.first_name) + str(update.effective_user.last_name)
    udb.add_user(User(chat_id=chat_id, date=t, full_name=full_name, user_name=user_name))
    udb.close()

    keys = ['posted_on_the_board', 'outside_board']
    reply_buttons = tools.constr_btn(keys, row=False)
    db = DataBase()
    all_posts = db.count_posts_after_time()
    t = update.message.date
    new_posts = db.count_posts_after_time(t)
    db.close()
    text = console.start(update._effective_user.first_name, all_posts=all_posts, new_posts=new_posts)
    update.message.delete()
    update.message.reply_text(text=text, reply_markup=reply_buttons, parse_mode='HTML')


def reload_posts(update: Update, context: CallbackContext) -> None:
    t = update.message.date
    channel_scraper.reload(t)
    update.message.reply_text(text="Successfuly reloaded!", parse_mode='HTML')


def summary(update: Update, context: CallbackContext) -> None:
    t = update.message.date
    sums = tools.user_summary(t, 20)
    text = "\n".join(sums)
    update.message.reply_text(text=text, parse_mode='HTML')


def invalid_cmd(update: Update, context: CallbackContext) -> None:
    update.message.delete()
