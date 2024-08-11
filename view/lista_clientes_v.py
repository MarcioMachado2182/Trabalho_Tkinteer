import tkinter as tk
from tkinter import ttk
from controller.cliente_c import listar_clientes

class ListaClientesView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Clientes")
        self.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("Nome", "CPF", "Email"), show='headings')
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Email", text="Email")
        self.tree.pack(expand=True, fill='both')

        self.populate_tree()

        tk.Button(self, text="Voltar", command=self.voltar).pack(pady=10)

    def populate_tree(self):
        for row in listar_clientes():
            self.tree.insert("", tk.END, values=row)

    def voltar(self):
        self.destroy()
        from view.tela_inicial_v import TelaInicialView
        TelaInicialView().mainloop()
