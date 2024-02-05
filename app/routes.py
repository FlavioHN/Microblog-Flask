from app import app
from flask import render_template

@app.route('/')

#@app.base('/base')
#def base():
#    return render_template('base.html')
@app.route('/index', defaults={'nome': 'usuario'})
@app.route('/index/<nome>')
def index(nome):
    #nome = "Fulano de Tals"
    dados = {"framework": "Flask", "linguagem": "Python"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')



if __name__ == "__main__":
    app.run(debug=True)