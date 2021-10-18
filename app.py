import json

from flask import Flask, render_template
import requests
app = Flask(__name__)

apikey = 'f3463a88067a455892363f8ead0bd700'


gameName = 'Mega Man 6'
search = f'&search={gameName}'
url = f'https://api.rawg.io/api/games?key={apikey}{search}'
request = requests.get(url)
data = request.json()
print(data['results'][0]['background_image'])

# for i in range(50):
#     datajson = request.json()['results'][i]['games']
#    for item in datajson:
#       i += 1
#        print(item['name'])



@app.route('/')
def login():  # put application's code here
    apikey = 'f3463a88067a455892363f8ead0bd700'
    request = requests.get(f'https://api.rawg.io/api/platforms?key={apikey}')
    datajson = request.json()['results'][1]
    print(datajson)
    return render_template("login.html")


@app.route('/index.html')
def index():  # put application's code here
    i = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    return render_template("index.html", i=i)


if __name__ == '__main__':
    app.run()
