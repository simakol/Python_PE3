# import random


# def get_random_int(min, max):
#     return random.randint(min, max)


# print(get_random_int(100, 500))
# print(get_random_int(1, 5))
# print(get_random_int(-5, 0))

import tkinter as tk


def get_text():
    label["text"] = message.get()


window = tk.Tk()  # створення головного елементу інтерфейсу - вікна

window.title("Це заголовок моєї програми")  # створює заголовок вікна програми

# задаємо розміри та відстпупи вікна: 400 - ширина, 200 - висота, 450 - відступ зліва, 300 - відступ зверху
window.geometry("400x200+450+300")

window.resizable(0, 0)  # забороняю змінювати розміри вікна

window.configure(bg="grey")

greeting = tk.Label(text="Hello, world!", bg="green",
                    fg="black", font="Arial 50 bold")

greeting.pack()  # розмістити віджет на вікні

message = tk.StringVar() # контейнер для нашого тексту
entry = tk.Entry(textvariable=message)
entry.pack()

label = tk.Label(text="Тут буде ваш текст")
label.pack()

tk.Button(text="Click", command=get_text).pack()


window.mainloop()  # це нескінченний цикл, який не дає нашій програмі закритись
