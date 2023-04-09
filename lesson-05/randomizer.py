import tkinter as tk
import random


def get_random_int(min, max):
    return random.randint(min, max)


def update_number():
    number_label["text"] = get_random_int(-100, 100)


window = tk.Tk()
window.title("Randomizer")
window.geometry("400x200+500+250")
window.resizable(0, 0)
window.configure(bg="#05C3DD")

number_label = tk.Label(text="Ваше число", bg="#05C3DD",
                        fg="yellow", font="Arial 50 bold")
number_label.pack()

tk.Button(text="Згенерувати", fg="black", bd="0", font="Arial 25",
          padx="10", pady="8", command=update_number).pack()

window.mainloop()
