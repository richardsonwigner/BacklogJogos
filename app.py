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

jogo1 = Jogo('Mega Man 10(2010)', 'https://media.rawg.io/media/screenshots/b87/b876d9664840d7e2f53cf5c649476935.jpg',
             '2')
jogo2 = Jogo('Valorant', 'https://media.rawg.io/media/games/b11/b11127b9ee3c3701bd15b9af3286d20e.jpg', '4')
jogo3 = Jogo('The Sims 4', 'https://media.rawg.io/media/games/e44/e445335e611b4ccf03af71fffcbd30a4.jpg', '10')
jogo4 = Jogo('ARK: Survival Evolved', 'https://media.rawg.io/media/games/58a/58ac7f6569259dcc0b60b921869b19fc.jpg',
             '10')

ListJogo = [jogo1, jogo2, jogo3, jogo4]

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
    datajson = requestapi.json()['results']
    return render_template("index.html", datajson=datajson, ListJogo=ListJogo)


@app.route('/editar', methods=['POST', ])
def telaEditar():  # put application's code here
    name_jogo = request.form['nomeJogo']
    for jogo in ListJogo:
        if (name_jogo == jogo.nomeJogo):
            return render_template("editar.html", jName=jogo.nomeJogo, jImg=jogo.imgJogo)


@app.route('/editarJogo', methods=['POST', ])
def editarJogo():  # put application's code here
    name_jogo = request.form['nomeJogo']
    nota_jogo = request.form['notaJogo']
    for jogo in ListJogo:
        if (name_jogo == jogo.nomeJogo):
            if not nota_jogo == 'Nota':
                jogo.notaJogo = nota_jogo
                flash('Editado com sucesso!')
    return redirect('/index')

@app.route('/deletar/<string:name>')
def deletar(name):
    for jogo in ListJogo:
        if jogo.nomeJogo == name:
            ListJogo.remove(jogo)
    return redirect('/index')


@app.route('/adicionar')
def telaAdicionar():  # put application's code here
    return render_template("adicionar.html")


if __name__ == '__main__':
    app.run()
