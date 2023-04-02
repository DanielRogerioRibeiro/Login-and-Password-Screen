# Tela de Login e Senha
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import customtkinter




#Colors

cor1 = "white"
cor2 = "#bfb911" #gold
cor3 = "black"

customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("dark-blue")


# Janela de login
window = customtkinter.CTk()
window.title     ("AI QUE LINDO - LOGIN")
window.geometry  ('487x383') 
#window.iconphoto (PhotoImage(file="imagens/aiquelindo1.png"))
window.resizable (width=True,height=True)


img = PhotoImage (file="imagens/aiquelindo-487-383.png")

Label.logo = Label(window, image=img, width=487, height=383, border=None)
Label.logo.pack()


#Credenciais
credenciais = ["joao", "123456"]

def verificar_senha():
    nome = e_name.get()
    senha = e_pass.get()

    if nome == "admin" and senha == "admin":
        messagebox.showinfo("Login", "Seja bem vindo Admin !!!")
        
    elif credenciais[0] == nome and credenciais[1]== senha:	
        messagebox.showinfo("Login", "Olá...Seja bem vindo de Volta" +credenciais[0])
                
    else:
        messagebox.showwarning("Erro", "Verifique o Nome e/ou Senha")



#Configurando Email/Login
label_name = customtkinter.CTkLabel(window, width=20, height=10, text="Name: *", anchor=NW, font=('Ivy', 12))
label_name.place(x=50, y=80)
e_name = customtkinter.CTkEntry(window, placeholder_text="Entry your Name", width=250, height=30, show="", justify='left', font=('', 10), border_width=0, corner_radius=10)
e_name.place(x=50, y=100)

#Configurando Password
label_pass = customtkinter.CTkLabel(window, width=20, height=10, text="Password *", anchor=NW, font=('Ivy', 12))
label_pass.place(x=50, y=155)
e_pass = customtkinter.CTkEntry(window, placeholder_text="Entry your Password" , width=250, height=30, show="*", justify='left', font=('', 10), border_width=0, corner_radius=10)
e_pass.place(x=50, y=175)

checkbox = customtkinter.CTkCheckBox(window, checkbox_height=13, checkbox_width=13 , text="Lembrar Login")
checkbox.place(x=250, y=230, anchor=CENTER)

b_confirmar = customtkinter.CTkButton(window, command=verificar_senha, text="ENTRAR", width=150, height=32, border_width=0, corner_radius=10)
b_confirmar.place(x=250, y=270, anchor=CENTER)




window.mainloop()
