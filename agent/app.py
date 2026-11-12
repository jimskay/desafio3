import sqlite3
import hashlib

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor  = conexao.cursor()

    # Hash da senha fornecida para comparação com o hash armazenado
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    query = "SELECT * FROM usuarios WHERE username = ? AND password_hash =?"    

    cursor.execute(query, (usuario, senha_hash))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."