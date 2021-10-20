import json
from Classes import User
from flask import Flask, render_template, request, redirect, session, flash
import requests

from Classes.Jogo import Jogo

app = Flask(__name__)

apikey = 'f3463a88067a455892363f8ead0bd700'
app.secret_key = 'secretKey'

# gameName = 'Mega Man 6'
# search = f'&search={gameName}'
# url = f'https://api.rawg.io/api/games?key={apikey}{search}'
# requestapi = requests.get(url)
# data = requestapi.json()
# print(data['results'][0]['background_image'])

url = f'https://api.rawg.io/api/games?key={apikey}'
requestapi = requests.get(url)

user1 = User.User('1', 'user1', '123')
user2 = User.User('2', 'user2', '123')

ListUsers = [user1, user2]

ListJogo = []


@app.route('/')
def login():  # put application's code here
    return render_template("login.html")


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    user_name = request.form['user']
    password_user = request.form['password']
    for user in ListUsers:
        if user.nome == user_name and user.senha == password_user:
            return redirect('/index')
        else:
            flash('Erro no login')
            return redirect('/')


@app.route('/addJogo', methods=['POST', ])
def addJogo():
    name_jogo = request.form['nomeJogo']
    nota_jogo = request.form['notaJogo']
    search = f'&search={name_jogo}'
    url = f'https://api.rawg.io/api/games?key={apikey}{search}'
    requestapi = requests.get(url)
    data = requestapi.json()
    img_jogo = data['results'][0]['background_image']
    name_jogo = data['results'][0]['name']

    jogoEncontrado = Jogo(name_jogo, img_jogo, nota_jogo)
    ListJogo.append(jogoEncontrado)
    return redirect('/index')


@app.route('/index')
def index():  # put application's code here
    # gameName = 'Mega Man 6'
    # search = f'&search={gameName}'
    # url = f'https://api.rawg.io/api/games?key={apikey}{search}'
    # requestapi = requests.get(url)
    # data = requestapi.json()
    # imagemjogo = data['results'][0]['background_image']

    # for i in range(10):
    datajson = requestapi.json()['results']
    return render_template("index.html", datajson=datajson)


@app.route('/editar')
def telaEditar():  # put application's code here
    return render_template("editar.html")


@app.route('/adicionar')
def telaAdicionar():  # put application's code here
    return render_template("adicionar.html")


if __name__ == '__main__':
    app.run()
