import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller.funcionario_c import save_funcionario

class CadastroFuncionarioView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Funcionário")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Carregar e configurar a imagem de fundo
        bg_image = Image.open("midia/Feeling.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_photo  # Manter uma referência para evitar a coleta de lixo

        tk.Label(self, text="Nome", bg="white").pack(pady=5)
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack(pady=5)

        tk.Label(self, text="Matrícula", bg="white").pack(pady=5)
        self.matricula_entry = tk.Entry(self)
        self.matricula_entry.pack(pady=5)

        tk.Label(self, text="Senha", bg="white").pack(pady=5)
        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack(pady=5)

        tk.Label(self, text="CPF", bg="white").pack(pady=5)
        self.cpf_entry = tk.Entry(self)
        self.cpf_entry.pack(pady=5)

        tk.Button(self, text="Cadastrar", command=self.cadastrar_funcionario).pack(pady=10)
        tk.Button(self, text="Voltar", command=self.voltar).pack(pady=10)

    def cadastrar_funcionario(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        senha = self.senha_entry.get()
        cpf = self.cpf_entry.get()

        if not (nome and matricula and senha and cpf):
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
            return

        result = save_funcionario(nome, matricula, senha, cpf)
        messagebox.showinfo("Info", result)
        self.clear_entries()

    def clear_entries(self):
        self.nome_entry.delete(0, tk.END)
        self.matricula_entry.delete(0, tk.END)
        self.senha_entry.delete(0, tk.END)
        self.cpf_entry.delete(0, tk.END)

    def voltar(self):
        self.destroy()
        from view.tela_inicial_v import TelaInicialView
        TelaInicialView().mainloop()
