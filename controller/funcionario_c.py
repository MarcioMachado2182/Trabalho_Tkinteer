from model.database import get_all_funcionarios, save_funcionario

def listar_funcionarios():
    return get_all_funcionarios()

def cadastrar_funcionario(nome, matricula, senha, cpf):
    return save_funcionario(nome, matricula, senha, cpf)
