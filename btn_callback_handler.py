from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext

from configparser import ConfigParser
import random

import tools
import commands
import console
from database import DataBase, UserDatabase
from user import User



def btn_response(update: Update, context: CallbackContext) -> None:

    update.callback_query.answer()

    call_back = update.callback_query.data
    print(update.callback_query.message.date)
    if call_back == 'restart':
        restart(update)
    elif call_back in commands.nav_map.keys():
        nav_responder(update, call_back)
    elif call_back in commands.back_map.keys():
        nav_responder(update, commands.back_map[call_back])
    else:
        photo_displayer(update, call_back)

def nav_responder(update: Update, call_back: str) -> None:
    keys = commands.nav_map[call_back]
    reply_btns = tools.constr_btn(keys, row=False if call_back=='top_menu' else True)
    update.callback_query.message.edit_text("<b>"+
        "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"+
        console.reply_titles[call_back]+
        "\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"+
        "</b>", reply_markup=reply_btns, parse_mode='HTML')


def photo_displayer(update: Update, call_back: str) -> None:

    update.callback_query.message.edit_text(
        "\n🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸\n<b>"+
        console.reply_titles[call_back]+
        "</b>\n🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹", parse_mode='HTML')

    db = DataBase()
    if call_back in commands.categories:
        data = db.filter_by_category(call_back)

    elif call_back in commands.main_category:
        time_id, category = call_back.split('_')
        if time_id == 'new':
            t = update.callback_query.message.date
            data = db.filter_by_cat_and_time(category=category, time=t)
        else:
            data = db.filter_by_cat_and_time(category=category)
    else:
        t = update.callback_query.message.date
        if call_back == 'outside_board_all_ads':
            data = db.filter_by_date(place_posted=db.tables[1], posted_date=True,time=datetime.fromtimestamp(0), before=False)
        elif call_back == 'outside_board_new_ads':
            data = db.filter_by_date(place_posted=db.tables[1], posted_date=True, time=t, before=False)
        elif call_back == 'on_board_all_ads':
            data = db.filter_by_date(place_posted=db.tables[0], posted_date=True, time=datetime.fromtimestamp(0), before=False)
        else:
            data = db.filter_by_date(place_posted=db.tables[0], posted_date=True, time=t, before=False)

    send_photo(update, data)
    db.close()
    if len(data):
        show_advert(update)
    after_display(update, commands.sent_img_signals[call_back], len(data))


def send_photo(update: Update, data: list):
        if len(data):
            for item in data:
                caption = item.description if item.description else console.btn_options[item.category]
                update.callback_query.message.reply_photo(entity+str(item.post_id), caption=caption)
        else:
            update.callback_query.message.reply_text("<u><pre><i>ለጊዜው በዚህ ዘርፍ ማስታዎቂያ አልተለጠፈም</i></pre></u>", parse_mode='HTML')


def after_display(update: Update, back_to: str, number_len: int):
    keys = ['top_menu', back_to, 'stop']
    btns = tools.constr_btn(keys, key_id=back_to)
    update.callback_query.message.reply_text(f"{number_len} ምስል(ሎች) ታይተዋል", reply_markup=btns, parse_mode='HTML')


def restart(update: Update):
        udb = UserDatabase()
        udb.create_table()
        chat_id = update.callback_query.message.chat_id
        t = update.callback_query.message.date
        user_name = str(update.effective_user.username)
        full_name = str(update.effective_user.first_name) + str(update.effective_user.last_name)
        udb.add_user(User(chat_id=chat_id, date=t, user_name=user_name, full_name=full_name))
        udb.close()

        keys = ['posted_on_the_board', 'outside_board']
        reply_btns = tools.constr_btn(keys, row=False)
        db = DataBase()
        all_posts = db.count_posts_after_time()
        t = update.callback_query.message.date
        new_posts = db.count_posts_after_time(t)
        db.close()
        text = console.start(update._effective_user.first_name, all_posts=all_posts, new_posts=new_posts)
        update.callback_query.message.edit_text("<b>"+text+"</b>", reply_markup=reply_btns, parse_mode='HTML')


def show_advert(update: Update) -> None:
    db = DataBase()
    data = db.filter_by_category("ads")
    show = random.randint(0, 1)
    if data and not show:
        current_ad = random.choice(data)
        caption = "#Advertisment\n\n" + current_ad.description
        update.callback_query.message.reply_photo(entity+str(current_ad.post_id), caption=caption)

    db.close()

config = ConfigParser()
config.read("files/config.ini")
entity = config["Telegram"]["entity"]
