import tkinter as tk
from PIL import Image, ImageTk
from view.cadastro_funcionario_v import CadastroFuncionarioView
from view.cadastro_cliente_v import CadastroClienteView
from view.lista_funcionarios_v import ListaFuncionariosView
from view.lista_clientes_v import ListaClientesView
from view.login_v import LoginView

class TelaInicialView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela Inicial")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        # Carregar e configurar a imagem de fundo
        bg_image = Image.open("midia/Feeling.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
        bg_label.image = bg_photo  # Manter uma referência para evitar a coleta de lixo

        tk.Button(self, text="Cadastrar Funcionário", command=self.cadastro_funcionario).pack(pady=10)
        tk.Button(self, text="Exibir Lista de Funcionários", command=self.exibir_funcionarios).pack(pady=10)
        tk.Button(self, text="Cadastrar Cliente", command=self.cadastro_cliente).pack(pady=10)
        tk.Button(self, text="Exibir Lista de Clientes", command=self.exibir_clientes).pack(pady=10)
        tk.Button(self, text="Voltar para Login", command=self.voltar_login).pack(pady=10)
        tk.Button(self, text="Sair do Sistema", command=self.sair_sistema).pack(pady=10)

    def cadastro_funcionario(self):
        self.destroy()
        CadastroFuncionarioView().mainloop()

    def exibir_funcionarios(self):
        self.destroy()
        ListaFuncionariosView().mainloop()

    def cadastro_cliente(self):
        self.destroy()
        CadastroClienteView().mainloop()

    def exibir_clientes(self):
        self.destroy()
        ListaClientesView().mainloop()

    def voltar_login(self):
        self.destroy()
        LoginView().mainloop()

    def sair_sistema(self):
        self.destroy()
        self.quit()  # Encerrar a aplicação
