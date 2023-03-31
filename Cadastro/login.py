# Tela de Login e Senha
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


#Colors

cor1 = "white"
cor2 = "gold"
cor3 = "black"


# Janela de login
window = Tk()
window.title     ("AI QUE LINDO - LOGIN")
window.geometry  ('600x350') 
window.iconphoto (False, PhotoImage(file="imagens/aiquelindo.png"))
window.resizable (width=True,height=True)

img = PhotoImage (file="imagens/aiquelindo.png")

Label.logo = Label(window, image=img).pack(anchor="center")


#Configurando o frame cima
label_login = Label(window, text="LOGIN", anchor=NE, font=('Ivy 25 bold'), fg=cor2, bg=None)
label_login.place(x=5, y=5)


#Credenciais
credenciais = ["joao", "123456"]

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Seja bem vindo Admin !!!")
        
    elif credenciais[0] == nome and credenciais[1]== senha:	
        messagebox.showinfo("Login", "Seja bem vindo de Volta" +credenciais[0])
        
    else:
        messagebox.showwarning("Erro", "Verifique o nome e a senha")



#Configurando o frame baixo
label_nome = Label(window, text="NOME *", anchor=NW, font=('Ivy 10'), fg=cor3)
label_nome.place(x=50, y=60)
e_nome = Entry(window, width=25, justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
e_nome.place(x=50, y=100)


label_pass = Label(window, text="PASSWORD *", anchor=NW, font=('Ivy 10'), fg=cor3)
label_pass.place(x=50, y=150)
e_pass = Entry(window, width=25, show="*", justify='left', font=('', 15), highlightthickness=1, relief=SOLID)
e_pass.place(x=50, y=190)


b_confirmar = Button(window, command=verificar_senha, text="ENTRAR", width=39, height=2, font=('Ivy 8 bold'), fg=cor3, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=160, y=300)




window.mainloop()
