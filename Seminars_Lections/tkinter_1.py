from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
root.resizable(True, False)
label = Label(text="Привет! Давай поработаем с файлами)") # создаем текстовую метку
label.pack()    # размещаем метку в окне
# icon = PhotoImage(file = "DogN.png")
# root.iconphoto(False, icon)
 
root.mainloop()