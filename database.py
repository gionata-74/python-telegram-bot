import sqlite3
from datetime import datetime, timedelta

from post_item import PostItem
from user import User
from commands import table_lst


class DataBase:

    tables = table_lst
    def __init__(self, path="files/posts.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_tables(self) -> None:
        with self.conn:
            for table in self.tables:
                self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS {table} (
                    post_id INTEGER NOT NULL PRIMARY KEY,
                    category TEXT NOT NULL,
                    posted_date INTEGER NOT NULL,
                    exp_date INTEGER NOT NULL,
                    description TEXT DEFAULT NULL
                ); """)

    def add_item(self, place_posted: str, item: PostItem) -> None:
        with self.conn:
            self.cursor.execute(f"SELECT * FROM {place_posted} WHERE post_id = :post_id;", \
                {"post_id":item.post_id})

            if (not self.cursor.fetchone()):
                self.cursor.execute(f"INSERT INTO {place_posted} VALUES \
                    (:post_id, :category, :posted_date, :exp_date, :description);",
                        {
                            'post_id': item.post_id,
                            'category': item.category,
                            'posted_date': item.posted_date.timestamp(),
                            'exp_date': item.exp_date.timestamp(),
                            'description': item.description
                        }
                )

    def del_item(self, place_posted, item) -> None:
        with self.conn:
            self.cursor.execute(f"DELETE FROM {place_posted} WHERE post_id = :post_id;", \
                {"post_id": item.post_id})

    def filter_by_date(self, place_posted, time=datetime.fromtimestamp(0), exp_date=False, posted_date=False, before=True) -> list:
        matches = []
        date = time.date()
        date = datetime(date.year, date.month, date.day).timestamp()
        with self.conn:
            if posted_date:
                if before:
                    self.cursor.execute(f"SELECT * FROM {place_posted} WHERE posted_date < :date", {'date': date})
                else:
                    self.cursor.execute(f"SELECT * FROM {place_posted} WHERE posted_date >= :date", {'date': date})
            elif exp_date:
                if before:
                    self.cursor.execute(f"SELECT * FROM {place_posted} WHERE exp_date < :date", {'date': date})
                else:
                    self.cursor.execute(f"SELECT * FROM {place_posted} WHERE exp_date >= :date", {'date': date})
            if exp_date or posted_date:
                data = self.cursor.fetchall()
                for item in data:
                    if item[1] != "ads":
                        matches.append(PostItem(
                            post_id=item[0],
                            category=item[1],
                            posted_date=item[2],
                            exp_date=item[3],
                            description=item[4])
                            )
        return matches

    def filter_by_category(self, category: str) -> list:
        matches = []
        with self.conn:
            self.cursor.execute(f"SELECT * FROM {self.tables[0]} WHERE category = :category", {'category': category})
            data = self.cursor.fetchall()
        for item in data:
                matches.append(PostItem(
                    post_id=item[0],
                    category=item[1],
                    posted_date=item[2],
                    exp_date=item[3],
                    description=item[4])
                    )
        return matches

    def filter_by_cat_and_time(self, category: str, time=datetime.fromtimestamp(0)):
        matches = []
        date = time.date()
        date = datetime(date.year, date.month, date.day).timestamp()
        with self.conn:
            self.cursor.execute(f"""SELECT * FROM {self.tables[0]} WHERE
                                category = :category AND posted_date > :posted_date""",
                                    {
                                        'category': category,
                                        'posted_date': date
                                    }
                                )
            data = self.cursor.fetchall()

        for item in data:
                matches.append(PostItem(
                    post_id=item[0],
                    category=item[1],
                    posted_date=item[2],
                    exp_date=item[3],
                    description=item[4])
                    )
        return matches

    @classmethod
    def count_posts_after_time(cls, time=datetime.fromtimestamp(0)):
        amount = 0
        database = cls()
        for table in cls.tables:
            amount += len(database.filter_by_date(table, time, posted_date=True, before=False))
        return amount

    def close(self):
        self.cursor.close()
        self.conn.close()


class UserDatabase:

    def __init__(self, path="files/user.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        with self.conn:
            self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS users (
                    date INTEGER NOT NULL PRIMARY KEY,
                    chat_id INTEGER NOT NULL,
                    full_name TEXT NOT NULL,
                    user_name TEXT
                ); """)

    def add_user(self, user: User):
        date = user.date.date()
        date = datetime(date.year, date.month, date.day).timestamp()
        with self.conn:
            self.cursor.execute(f" SELECT * FROM users WHERE chat_id = :chat_id AND date >= :date",
            {
                'chat_id':user.chat_id,
                'date': date
            }
            )
            data = self.cursor.fetchone()
            if (not data):
                self.cursor.execute(f"INSERT INTO users VALUES \
                    ( :date, :chat_id, :full_name, :user_name);",
                        {
                            'date': user.date.timestamp(),
                            'chat_id': user.chat_id,
                            'full_name': user.full_name,
                            'user_name': user.user_name
                        }
                )

    def get_daily_users(self, time: datetime, last_n_days: int) -> list:
        day = time.day
        month = time.month
        year = time.year

        daily_sessions = []
        one_day_sessions = []
        with self.conn:
            for i in range(last_n_days):
                date = datetime(year, month, day)-timedelta(days=i)
                nxt_date = (date + timedelta(days=1)).timestamp()
                date = date.timestamp()
                self.cursor.execute(f"SELECT * FROM users WHERE date > :date AND date <= :nxt_date", {'date': date, 'nxt_date': nxt_date})
                l_tuple_users = self.cursor.fetchall()
                for user in l_tuple_users:
                    one_day_sessions.append(User( date=user[0], chat_id=user[1], full_name=user[2], user_name=user[3]))
                daily_sessions.append(list(one_day_sessions))
                one_day_sessions.clear()
                l_tuple_users.clear()
        return daily_sessions




    def close(self):
        self.cursor.close()
        self.conn.close()

