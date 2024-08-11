from model.database import validate_user

def login(matricula, senha):
    return validate_user(matricula, senha)

