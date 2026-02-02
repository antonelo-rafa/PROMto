from flask import Flask, render_template, request, flash 

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



if __name__ == '__main__':
    app.run(debug=True)
