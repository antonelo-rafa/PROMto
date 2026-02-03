from flask import Flask, render_template, request, flash 
from bd import conexao_banco

app = Flask(__name__, template_folder='html')
app.secret_key = 'admin-promto'

#rota home
@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

#rota do login
@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('password')

    print(email, senha)
    return render_template('login.html')

#rota do cadastro:
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    email= request.form.get('email')
    senha= request.form.get('senha')

    conexao = conexao_banco()
    cursor = conexao.cursor()

    insert_cad = 'INSERT INTO cadastro(cpf, nome, email, senha) values(%s, %s, %s, %s)'
    valores = (cpf, nome, email, senha)

    cursor.execute(insert_cad, valores)
    conexao.commit()
    

if __name__ == '__main__':
    app.run(debug=True)
