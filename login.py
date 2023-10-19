
import customtkinter as ctk
from customtkinter import *
import customtkinter 
from tkinter import *

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()


    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de login")
        janela.iconbitmap("icon.ico")
        janela.resizable(False,False)


    def tela_login(self):
        #trabalhando com a imagem da tela
        img = PhotoImage(file="log.png")
        Label_img = ctk.CTkLabel(master=janela, image=img, text=None)
        Label_img.place(x=10, y=75)

        title_label = ctk.CTkLabel(master=janela, text="        Entre na sua conta e tenha \na plataforma", font=("Roboto", 20), text_color="#00B0F0"). place(x=15, y=10)

        #frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        #frame widgets dentro da tela de login
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("Roboto", 20))
        label.place(x=25, y=5)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuario", width=300, font=("Roboto", 14)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo de usuario é de carater obrigatório.", text_color="green", font=("Roboto", 9)).place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha de usuario", width=300, font=("Roboto", 14), show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo de usuario é de carater obrigatório.", text_color="green", font=("Roboto", 9)).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar sempre da senha").place(x=25, y=235)

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300).place(x=25, y=285)

        register_span = ctk.CTkLabel(master=login_frame, text="Se não tiver uma conta").place(x=25, y=325)
        register_button = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, fg_color="green",hover_color="#2D9334").place(x=175, y=325)

Application()

