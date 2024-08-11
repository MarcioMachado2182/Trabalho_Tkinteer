import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller.usuario_c import login

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Carregar e configurar a imagem de fundo
        bg_image = Image.open("midia/Feeling.png")  # Substitua pelo caminho da sua imagem
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_photo  # Manter uma referência para evitar a coleta de lixo

        tk.Label(self, text="Matrícula", bg="white").pack(pady=5)
        self.matricula_entry = tk.Entry(self)
        self.matricula_entry.pack(pady=5)

        tk.Label(self, text="Senha", bg="white").pack(pady=5)
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack(pady=5)

        tk.Button(self, text="Efetuar Login", command=self.perform_login).pack(pady=10)

    def perform_login(self):
        matricula = self.matricula_entry.get()
        senha = self.senha_entry.get()

        if login(matricula, senha):
            self.destroy()
            from view.tela_inicial_v import TelaInicialView
            TelaInicialView().mainloop()
        else:
            messagebox.showerror("Erro", "Matrícula ou senha inválidos")

