from model.database import get_all_clientes, save_cliente

def listar_clientes():
    return get_all_clientes()

def cadastrar_cliente(nome, cpf, endereco, bairro, cidade_estado, cep, telefone, email, senha):
    return save_cliente(nome, cpf, endereco, bairro, cidade_estado, cep, telefone, email, senha)
