from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates_folder')

# Armazenamento dos usuários e senhas
users = lambda: {
    "rafael": "123",
    "pedro": "456"
}

# Função lambda para processar o registro
register_user = lambda: users().update({request.form["username"]: request.form["password"]})

# Função lambda para verificar a senha
password_matches = lambda: users()[request.form["username"]] == request.form["password"]

# Função lambda para lidar com o login
login = lambda: "WELCOME " + request.form["username"] if password_matches() else "WRONG PASSWORD!!!!"

# Função lambda para processar a requisição
reqresp = lambda: register_user() if request.method == 'POST' else render_template('index.html')

app.add_url_rule('/index/', 'index', reqresp, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8080)
