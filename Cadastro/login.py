# Tela de Login e Senha
from tkinter import *


# Janela de login
window = Tk()
window.title     ("AI QUE LINDO - LOGIN")
window.geometry  ('600x350') 
window.iconphoto (False, PhotoImage(file="imagens/aiquelindo.png"))
window.resizable (width=True,height=True)

img = PhotoImage (file="imagens/aiquelindo.png")

Label.logo = Label(window, image=img).pack(anchor="center")






window.mainloop()
