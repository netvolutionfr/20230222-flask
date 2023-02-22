import json
import requests
from flask import Flask, jsonify

app = Flask(__name__)


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


NEWS_API_KEY = 'YOUR_API_KEY'
NEWS_API_URL = 'https://newsapi.org/v2/'

@app.route('/news')
def get_news():
    response = requests.get(NEWS_API_URL + 'top-headlines?country=fr&apiKey=' + NEWS_API_KEY)
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
