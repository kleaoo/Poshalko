import tkinter as tk

import time
# Создание главного окна:
from PIL import Image, ImageTk
root = tk.Tk()  # Основное окно
import tkinter as tk

root.title("Кликер")  # Надпись в топе окна
import screeninfo
root.geometry("700x350")  # Размер окна X
root.resizable(False, False)  # Запрещение изменения окна по X и Y
root.configure(bg="#d1ddde")  # Фон окна

n = 0  # Счётчик

image_path = "sigma.jpg"
def nplus():
    global n
    n += 1
    if n == 1:
        label1["text"] = str(n) + " Рубль."
    elif 1 < n <= 3:
        label1["text"] = str(n) + " Рубля."
    else:
        label1["text"] = str(n) + " Рублей."

def nsbros():
    global n
    n = 0
    label1["text"] = str(n) + " Рублей."

# Счётчик кликера:
label1 = tk.Label(root, text=str(n) + " Рублей.", font=("Helvetica 50"), background="#d1ddde")
label1.pack()

# Кнопка 1:
btn1 = tk.Button(text="Клик", background="#75a9fa", foreground="#fff",
                 padx="150", pady="10", font="16", command=nplus)
btn1.pack()

# Кнопка 2:
btn2 = tk.Button(text="Сброс", background="#e08e79", foreground="#fff",
                 padx="150", pady="10", font="16", command=nsbros)
btn2.pack()

root.mainloop()

if n == 3:
    imageS = Image.open(image_path)
else:
    print('dwufd')