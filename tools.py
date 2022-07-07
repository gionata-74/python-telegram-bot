from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from console import btn_options
from database import UserDatabase

def constr_btn(btn_keys: list, row=True, key_id='' ) -> list:
    btn_list = []
    if row:
        for key in btn_keys:
            btn_txt = '↩ ለመመለስ' if (key[:4]=='back') or (key_id==key) else btn_options[key]
            btn_list.append([InlineKeyboardButton(btn_txt, callback_data=key)])
        return InlineKeyboardMarkup(btn_list)

    for key in btn_keys:
        btn_list.append(InlineKeyboardButton('↩️ ለመመለስ' if (key[:4]=='back') or (key_id==key) else btn_options[key], callback_data=key))
    return InlineKeyboardMarkup([btn_list])


def user_summary(time: datetime, last_n_days: int) -> list:

    daily_users_amount = []
    all_users = set()

    db = UserDatabase()
    db.create_table()
    daily_users_list = db.get_daily_users(time, last_n_days)
    db.close()
    for one_day_users in daily_users_list:
        daily_users_amount.append(str(len(one_day_users)))
        for user in one_day_users:
            all_users.add(user.chat_id)
    daily_users_amount.append(str(len(all_users)))
    return daily_users_amount

