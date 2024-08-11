import tkinter as tk
from tkinter import ttk
from controller.funcionario_c import listar_funcionarios

class ListaFuncionariosView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Funcionários")
        self.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("Nome", "Matrícula", "CPF"), show='headings')
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Matrícula", text="Matrícula")
        self.tree.heading("CPF", text="CPF")
        self.tree.pack(expand=True, fill='both')

        self.populate_tree()

        tk.Button(self, text="Voltar", command=self.voltar).pack(pady=10)

    def populate_tree(self):
        for row in listar_funcionarios():
            self.tree.insert("", tk.END, values=row)

    def voltar(self):
        self.destroy()
        from view.tela_inicial_v import TelaInicialView
        TelaInicialView().mainloop()
