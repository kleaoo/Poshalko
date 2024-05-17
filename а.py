import time

from PIL import Image, ImageTk
import tkinter as tk
import screeninfo

# Путь к вашей картинке
image_path = "sigma.jpg"

# Создание главного окна tkinter
root = tk.Tk()

# Получение размеров экрана
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Загрузка и изменение размера картинки
imageS = Image.open(image_path)
imageS = imageS.resize((screen_width, screen_height))

# Конвертация картинки в формат, доступный для отображения в tkinter
image_tk = ImageTk.PhotoImage(imageS)

# Создание полноэкранного окна tkinter
root.attributes("-fullscreen", True)

# Создание виджета Label для отображения картинки в окне
label = tk.Label(root, image=image_tk)
label.pack(fill="both", expand=True)

# Запуск главного цикла окна
root.mainloop()
playsound('SigmaSong.mp3')

time.sleep(1)
dir(imageS)