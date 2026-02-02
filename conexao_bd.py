import mysql.connector
def conexao_banco():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        port='8889',
        database = 'login2'
    )
    return conexao

conexao = conexao_banco()
cursor = conexao.cursor()

print(conexao, 'conectado com sucesso')