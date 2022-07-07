import telegram
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.filedialog import askopenfilename


token = "1676328550:AAE8ujCMZvg4DLcF4xRYR4gLHcbS0AQSxwk"
base_url = "https://api.telegram.org/bot"

channel_name = "@asdfmilomIIOdfmBItpwomvsmcslei"

places = ['posted_on_the_board', 'outside_board']

categories = [
    "vacancy", "bid",
    "call", "missing",
    "assistance", "social",
    "product", "exhibition",
    "lottery", "educational",
    "meetings", "vital_event",
    "art", "other"
]


bot = telegram.Bot(token, base_url)

def post(place, category, deadline, path, desc):
    if (place in places) and (category in categories) and path and deadline:
        caption = formatter(place, category, deadline, path, desc)
        try:
            bot.send_photo(channel_name, open(f"{path}", 'rb'), caption=f"{caption}")
            lbl["fg"] = "green"
            lbl["text"] = "post uploaded!"
            combo_place.set("None")
            combo_place.select_clear()

            combo_cat.set("None")
            combo_cat.selection_clear()
            exp_date.selection_clear()
            entry.delete(0, "end")
            description.delete(1.0,"end")
        except:
            lbl["fg"] = "red"
            lbl["text"] = "Connection Error!"
    else:
        lbl["fg"] = "red"
        lbl["text"] = "Invalid Entry! not uploaded"


def formatter(place, category, exp_date, path, description):
    exp_date = exp_date.split("/")
    return f"{place}, {category}, {exp_date[1]}/{exp_date[0]}/20{exp_date[2]}, {description}"


def upload(event):
    filename = askopenfilename()
    entry.insert(0, filename)
    


root = tk.Tk()
root.title("Post On Channel")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = tk.Frame(root, bg="gold")
main_frame.grid(row=0, column=0, sticky="ewsn")
main_frame.rowconfigure(3, weight=0, minsize=40)
main_frame.rowconfigure(1, weight=0, minsize=40)
main_frame.rowconfigure(5, weight=1, minsize=250)
main_frame.columnconfigure(0, weight=0, minsize=450)
main_frame.columnconfigure(1, weight=1, minsize=400)

main_cat = tk.Label(main_frame, text="* Place of Post", bg="gold")
main_cat.grid(row=0, column=0, sticky="w", padx=5, pady=5)

combo_place = ttk.Combobox(main_frame)
combo_place["values"] = places
combo_place.set(" None")
combo_place.grid(row=1, column=0, sticky="ewns", padx=5, pady=5)


lbl_cat = tk.Label(main_frame, text="* Category", bg="gold")
lbl_cat.grid(row=2, column=0, sticky="w", padx=5, pady=5)

combo_cat = ttk.Combobox(main_frame)
combo_cat["values"] = categories
combo_cat.set(" None")

combo_cat.grid(row=3, column=0, sticky="ewns", padx=5, pady=5)

lbl_deadline = tk.Label(main_frame, text="* Deadline", bg="gold")
lbl_deadline.grid(row=4, column=0, sticky="w", padx=5, pady=5)

exp_date = Calendar(main_frame, year=2021)
exp_date.grid(row=5, column=0, sticky="ewsn", padx=5, pady=5)

# space
main_cat = tk.Label(main_frame, text="", bg="gold")
main_cat.grid(row=2, column=1, sticky="w", padx=5, pady=5)

main_cat = tk.Label(main_frame, text="", bg="gold")
main_cat.grid(row=3, column=1, sticky="w", padx=5, pady=5)


lbl_3 = tk.Label(main_frame, text="* Location", bg="gold")
lbl_3.grid(row=0, column=1, sticky="w", padx=5, pady=5)


upload_frame = tk.Frame(main_frame, bg="gold")
upload_frame.grid(row=1, column=1, sticky="ew", padx=0, pady=5)
upload_frame.rowconfigure(0, weight=1, minsize=15)
upload_frame.columnconfigure([0], weight=1, minsize=40)

entry = tk.Entry(upload_frame, width=40)
entry.grid(row=0, column=0, sticky="wens", padx=5)

upload_btn = ttk.Button(upload_frame, text="upload")
upload_btn.bind("<Button-1>", upload)
upload_btn.grid(row=0, column=1, sticky="ens", padx=5)


lbl = tk.Label(main_frame, text=" Description", bg="gold")
lbl.grid(row=4, column=1, sticky="w", padx=5, pady=5)


description = tk.Text(main_frame, bg="white", width=5, height=7)
description.grid(row=5, column=1, sticky="ewsn", padx=5, pady=5)


btn = ttk.Button(main_frame, text="Post")
btn.bind("<Button-1>", lambda x: post(
    combo_place.get(),
    combo_cat.get(),
    exp_date.get_date(),
    entry.get(),
    description.get("1.0","end-1c")))
btn.grid(row=6, column=1, pady=20)

lbl = tk.Label(main_frame, bg="gold")
lbl.grid(row=9, column=0, padx=5, pady=7, sticky="w")

root.update()
root.minsize((root.winfo_width()), (root.winfo_height())+100)
root.maxsize(1366, (root.winfo_height())+100)
root.mainloop()