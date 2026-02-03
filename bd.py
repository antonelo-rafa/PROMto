import mysql.connector
def conexao_banco():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        port='8889',
        database = 'promto'
    )
    return conexao