import json
from faker import Faker
import requests
from flask import Flask, jsonify

app = Flask(__name__)

fake = Faker(['fr_FR'])

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/test')
def test():
    return 'Test'


def get_current_user():
    return {'username': 'John',
            'email': 'john@example.com',
            'id': 1
            }


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    user = get_current_user()
    return 'User %s' % user.get('username')


NEWS_API_KEY = 'SECRET'
NEWS_API_URL = 'https://newsapi.org/v2/'

@app.route('/news')
def get_news():
    response = requests.get(NEWS_API_URL + 'everything?q=python&from=2023-01-22&sortBy=publishedAt&apiKey=' + NEWS_API_KEY)
    content = json.loads(response.content.decode('utf-8'))
    if response.status_code == 200:
        return jsonify({
            'status': 'success',
            'data': content
        })
    else:
        return jsonify({
            'status': 'error',
            'message': 'Error fetching news'
        })

METEO_API_KEY = 'SECRET'
METEO_API_URL = 'https://api.openweathermap.org/data/2.5/'

@app.route('/meteo/<city>')
def get_meteo(city):
    response = requests.get(METEO_API_URL + 'weather?q=' + city + '&appid=' + METEO_API_KEY)
    content = json.loads(response.content.decode('utf-8'))
    if response.status_code == 200:
        return jsonify({
            'status': 'success',
            'data': content
        })
    else:
        return jsonify({
            'status': 'error',
            'code': response.status_code,
            'message': 'Error fetching meteo'
        })


# Utiliser la librairie Faker pour générer des données aléatoires
liste_faker_personnes = []
for i in range(10):
    liste_faker_personnes.append({
        'id': i,
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
    })


@app.route('/personnes')
def get_personnes():
    return jsonify({
        'status': 'success',
        'data': liste_faker_personnes
    })


@app.route('/personnes/<int:id>')
def get_personne(id):
    return jsonify({
        'status': 'success',
        'data': liste_faker_personnes[id]
    })
