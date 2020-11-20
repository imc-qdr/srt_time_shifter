import tkinter as tk
from datetime import datetime, timedelta
import re


def shift_secs(file, sec, micro):
    pattern = r'(\d{2}:\d{2}:\d{2},d{3}$)|(\d{2}:\d{2}:\d{2})'
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()
        for i in range(len(text)):
            if re.match(pattern, text[i]):
                times = text[i].split(' --> ')
                times[1] = times[1].strip()
                objs = [(datetime.strptime(x, '%H:%M:%S,%f') +
                         timedelta(seconds=sec, microseconds=micro*1000)) for x in times]
                times_str = [datetime.strftime(x, '%H:%M:%S,%f')[:-3] for x in objs]
                line = ' --> '.join(times_str) + '\n'
                text[i] = line
    with open('new_'+file, 'w', encoding='utf-8') as f:
        f.writelines(text)


def shift():
    to_read = file.get()
    secs = int(sec.get())
    mirco_secs = int(mirco.get())
    shift_secs(to_read, secs, mirco_secs)


main = tk.Tk()
main.title("تحويل وقت الترجمة")
main.geometry('430x185')
main.resizable(0, 0)

file = tk.Entry(main, width=25)
file.grid(column=0, row=0, padx=20, pady=10, sticky='W')

file_label = tk.Label(main, text='اسم الملف مع الامتداد')
file_label.grid(column=0, row=1)

folder_label = tk.Label(main, text='(نفس المجلد)')
folder_label.grid(column=0, row=2)

sec = tk.Entry(main, width=15)
sec.grid(column=2, row=0, sticky="E")

sec_label = tk.Label(main, text="الثواني")
sec_label.grid(column=1, row=0, sticky="E")

mirco = tk.Entry(main, width=15)
mirco.grid(column=2, row=1, sticky="E")

mirco_label = tk.Label(main, text="أجزاء الثانية (واحد بالألف)")
mirco_label.grid(column=1, row=1, sticky="E")

button = tk.Button(main, text='ملف جديد', width=10, command=shift)
button.grid(columnspan=3, row=3, pady=(40, 10), padx=10)

aboud = tk.Label(main, text='احلى عبود')
aboud.grid(columnspan=3, row=4, padx=10, sticky='N')

tk.mainloop()
