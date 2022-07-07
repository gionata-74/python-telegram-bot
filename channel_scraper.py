from requests_html import HTMLSession
from datetime import datetime

from post_item import PostItem
from database import DataBase
from configparser import ConfigParser


def push_items(html, data_before: str, db: DataBase) -> None:
    while data_before:
        try:
            divs = html.find("div.tgme_widget_message_wrap.js-widget_message_wrap")
            for div in divs:
                try:
                    post_id = div.find("a.tgme_widget_message_photo_wrap", first=True)
                    post_id = post_id.attrs["href"].split("/")[4].split("?")[0]

                    posted_date = div.find("time.time", first=True).attrs["datetime"]
                    posted_date = datetime.strptime(posted_date,"%Y-%m-%dT%H:%M:%S+00:00")

                    caption = div.find("div.tgme_widget_message_text.js-message_text", first=True)
                    place_posted, category, exp_date, description = format_description(caption.text)

                    if post_id and place_posted and posted_date  and exp_date and category:
                        item = PostItem(
                            post_id=post_id,
                            category=category,
                            posted_date=posted_date,
                            exp_date=exp_date,
                            description=description
                            )              
                        db.add_item(place_posted, item)

                except Exception as e:
                    print("From channel_scraper.push_items unable to parse the posts: ", e)

            html = session.get(f"{url}?before={data_before}").html
        except Exception as e:
            print("From channel_scraper.push_items:", e) 
        try:   
            data_before = html.find("a.tme_messages_more.js-messages_more", first=True).attrs["data-before"]
            print(type(data_before))
        except:
            data_before=0 if data_before==1 else 1


def format_description(caption: str) -> tuple:
    try:
        data = caption.split(",")
        place_posted = (data[0]).strip()
        category = data[1].strip()
        exp_date = data[2].split("/")
        exp_date = datetime(int(exp_date[2]), int(exp_date[1]), int(exp_date[0]))
        try:
            description = data[3].strip()
        except:
            description = None
        return place_posted, category, exp_date, description
    except Exception as e:
        print("From Channel_scraper.format_description: ", e)
        return None, None, None


def scrap(db: DataBase) -> None:
    while True:
        try:
            html = session.get(url).html
            try:
                data_before = html.find("a.tme_messages_more.js-messages_more", first=True).attrs["data-before"]
            except:
                data_before = 1
            push_items(html, data_before, db)
            break
        except Exception as e:
            print("From channel_scraper", e)


def reload(time: datetime) -> None:
    db = DataBase()
    db.create_tables()
    scrap(db)
    for table in db.tables:
        matches = db.filter_by_date(table, time, before=True, exp_date=True)
        for match in matches:
            db.del_item(table, match)
    db.close()


session = HTMLSession()

config = ConfigParser()
config.read("files/config.ini")
url = config["Telegram"]["url"]


