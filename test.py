from flask import Flask, url_for, render_template, request, jsonify
import json
from pymongo import MongoClient
import sys

client = MongoClient()
TestDatabase = client.TestDatabase
users = TestDatabase.users
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print(request.form['email'], file=sys.stdout)
        email = request.form['email']
        password = request.form['password']
        cursor = users.find({"email": email, "password": password})
        if cursor and len(cursor) > 0:
            return 'Authenticated'
        return 'unknown user'


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
