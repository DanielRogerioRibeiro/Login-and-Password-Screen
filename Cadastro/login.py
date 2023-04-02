# Tela de Login e Senha
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import customtkinter




#Colors

cor1 = "#FFFFFF"
cor2 = "#cebd7f" #gold
cor3 = "black"
cor4 = "#1f1f1e" #transparente
cor5 = "#262626"

customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("dark-blue")


# Janela de login
window = Tk()
window.title     ("AI QUE LINDO - LOGIN")
window.geometry  ('487x383') 
window.iconphoto (False, PhotoImage(file="imagens/aiquelindo.png"))
window.resizable (width=False,height=False)


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
label_name = Label(window, width=5, height=2, text="Name: *", fg=cor1, font=('Ivy', 9), anchor=NW, background=cor4)
label_name.place(x=50, y=75)
e_name = customtkinter.CTkEntry(window, placeholder_text="Entry your Name", width=250, height=30, show="", justify='left', font=('', 10), corner_radius=10, bg_color=cor4)
e_name.place(x=50, y=100)

#Configurando Password
label_pass = Label(window, width=15, height=2, text="Password: *", fg=cor1, font=('Ivy', 9), anchor=NW, background=cor4)
label_pass.place(x=50, y=155)
e_pass = customtkinter.CTkEntry(window, placeholder_text="Entry your Password" , width=250, height=30, show="*", justify='left', font=('', 10), corner_radius=10, bg_color=cor4)
e_pass.place(x=50, y=175)

checkbox = customtkinter.CTkCheckBox(window, text="Lembrar Login", checkbox_width=15, checkbox_height=15, bg_color=cor4)
checkbox.place(x=100, y=230, anchor=CENTER)

b_confirmar = customtkinter.CTkButton(window, command=verificar_senha, text="ENTRAR", width=150, height=32, border_width=0, corner_radius=10, bg_color='blue')
b_confirmar.place(x=250, y=270, anchor=CENTER)




window.mainloop()
