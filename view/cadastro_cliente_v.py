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

        # Criar um frame para os botões e posicioná-lo na parte inferior
        button_frame = tk.Frame(self, bg='white')
        button_frame.pack(side=tk.BOTTOM, pady=10)

        # Adicionar botão de cadastrar
        tk.Button(button_frame, text="Cadastrar", command=self.cadastrar, bg='#4CAF50', fg='white', relief='raised').pack(side=tk.LEFT, padx=5)

        # Adicionar botão de voltar
        tk.Button(button_frame, text="Voltar", command=self.voltar, bg='#f44336', fg='white', relief='raised').pack(side=tk.LEFT, padx=5)

    def cadastrar(self):
        cliente_data = {label: entry.get() for label, entry in self.entries.items()}

        if all(cliente_data.values()):
            success = cadastrar_cliente(
                cliente_data['Nome'],
                cliente_data['CPF'],
                cliente_data['Endereço'],
                cliente_data['Bairro'],
                cliente_data['Cidade/Estado'],
                cliente_data['CEP'],
                cliente_data['Telefone'],
                cliente_data['Email'],
                cliente_data['Senha']
            )
            
            if "sucesso" in success.lower():
                messagebox.showinfo("Sucesso", success)
                self.limpar_campos()
            else:
                messagebox.showerror("Erro", success)
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos")

    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def voltar(self):
        self.destroy()
        from view.tela_inicial_v import TelaInicialView
        TelaInicialView().mainloop()
