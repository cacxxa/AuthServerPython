#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from auth import Auth
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

auth = Auth()

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    encoded = auth.getJWT(data['username'])
    return jsonify(
        {
            'user': data['username'],
            'jwt': str(encoded)
        })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
