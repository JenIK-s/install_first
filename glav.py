from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def install_browsers():
    global browsers_image
    browsers = Toplevel(root)
    browsers.title('Браузеры')
    browsers.mainloop()


def install_utilities():
    utilities = Toplevel(root)
    utilities.title('Утилиты')
    utilities.mainloop()


def insatall_editors():
    editors = Toplevel(root)
    editors.title('Редакторы')
    editors.mainloop()


def install_walkman():
    walkman = Toplevel(root)
    walkman.title('Плееры')
    walkman.mainloop()


def install_activators():
    activators = Toplevel(root)
    activators.title('Активаторы')
    activators.mainloop()
# ----------------------Главное окно----------------------
root = Tk()
root.geometry('490x100')
root.title('Install_F')

browsers_image = ImageTk.PhotoImage(Image.open('browser.png'))
utilities_image = ImageTk.PhotoImage(Image.open('utility.png'))
editors_image = ImageTk.PhotoImage(Image.open('editors.png'))
walkman_image = ImageTk.PhotoImage(Image.open('walkman.png'))
activators_image = ImageTk.PhotoImage(Image.open('activators.png'))

style = ttk.Style()
style.configure('my.TButton', font=('Corbel', 11))

# ----------------------Браузеры----------------------
root_label_image_b = Label(root, image=browsers_image)
root_label_image_b.grid(row=0, column=0)

root_button_browsers = ttk.Button(root, text='Браузеры', command=install_browsers, style='my.TButton')
root_button_browsers.grid(row=1, column=0)
# ----------------------Утилиты----------------------
root_label_image_u = Label(root, image=utilities_image)
root_label_image_u.grid(row=0, column=1)

root_button_utilities = ttk.Button(root, text='Утилиты', command=install_utilities, style='my.TButton')
root_button_utilities.grid(row=1, column=1)
# ----------------------Редакторы----------------------
root_label_image_e = Label(root, image=editors_image)
root_label_image_e.grid(row=0, column=2)

root_button_editors = ttk.Button(root, text='Редакторы', command=insatall_editors, style='my.TButton')
root_button_editors.grid(row=1, column=2)
# ----------------------Плееры----------------------
root_label_image_w = Label(root, image=walkman_image)
root_label_image_w.grid(row=0, column=3)

root_button_walkman = ttk.Button(root, text='Плееры', command=install_walkman, style='my.TButton')
root_button_walkman.grid(row=1, column=3)
# ----------------------Активаторы----------------------
root_label_image_a = Label(root, image=activators_image)
root_label_image_a.grid(row=0, column=4)

root_button_activators = ttk.Button(root, text='Активаторы', command=install_activators, style='my.TButton')
root_button_activators.grid(row=1, column=4)
root.mainloop()
