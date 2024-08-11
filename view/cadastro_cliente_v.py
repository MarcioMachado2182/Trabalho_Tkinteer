import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from controller.cliente_c import cadastrar_cliente

class CadastroClienteView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Clientes")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Carregar e configurar a imagem de fundo
        bg_image = Image.open("midia/Feeling.png")  # Substitua pelo caminho da sua imagem
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_photo  # Manter uma referência para evitar a coleta de lixo

        # Criar um frame para os campos de entrada
        form_frame = tk.Frame(self, bg='white')
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Configurar o grid para os campos de entrada
        labels = ["Nome", "CPF", "Endereço", "Bairro", "Cidade/Estado", "CEP", "Telefone", "Email", "Senha"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(form_frame, text=label, bg='white').grid(row=i, column=0, padx=10, pady=5, sticky='e')
            entry = tk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
            self.entries[label] = entry

        # Adicionar botão de cadastrar
        tk.Button(self, text="Cadastrar", command=self.cadastrar, bg='#4CAF50', fg='white', relief='raised').pack(pady=10)

        # Adicionar botão de voltar
        tk.Button(self, text="Voltar", command=self.voltar, bg='#f44336', fg='white', relief='raised').pack(pady=10)
    def cadastrar(self):
        cliente_data = {label: entry.get() for label, entry in self.entries.items()}

        # Adicionar validação de dados aqui se necessário

        if all(cliente_data.values()):
            success = cadastrar_cliente(cliente_data)
            if success:
                messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso")
                self.limpar_campos()
            else:
                messagebox.showerror("Erro", "Falha ao cadastrar cliente")
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos")

    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def voltar(self):
        self.destroy()
        from view.tela_inicial_v import TelaInicialView
        TelaInicialView().mainloop()
