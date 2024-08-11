import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user="marcio_2182",
        password="2182",
        host="localhost",
        port=3306,
        database="cadastro"
    )

def validate_user(matricula, senha):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM funcionarios WHERE matricula = %s AND senha = %s",
            (matricula, senha)
        )
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        return False
    finally:
        cursor.close()
        conn.close()

def save_funcionario(nome, matricula, senha, cpf):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO funcionarios (nome, matricula, senha, cpf) VALUES (%s, %s, %s, %s)",
            (nome, matricula, senha, cpf)
        )
        conn.commit()
        return "Funcionário cadastrado com sucesso."
    except mysql.connector.Error as err:
        return f"Erro: {err}"
    finally:
        cursor.close()
        conn.close()

def save_cliente(nome, cpf, endereco, bairro, cidade_estado, cep, telefone, email, senha):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, cpf, endereco, bairro, cidade_estado, cep, telefone, email, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (nome, cpf, endereco, bairro, cidade_estado, cep, telefone, email, senha)
        )
        conn.commit()
        return "Cliente cadastrado com sucesso."
    except mysql.connector.Error as err:
        return f"Erro: {err}"
    finally:
        cursor.close()
        conn.close()

def get_all_funcionarios():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT nome, matricula, cpf FROM funcionarios")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        return []
    finally:
        cursor.close()
        conn.close()

def get_all_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT nome, cpf, email FROM clientes")
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        return []
    finally:
        cursor.close()
        conn.close()

