from flask import Flask, jsonify
import requests

topic = 'pizza'

r= requests.get(f"https://newsdata.io/api/1/latest?apikey=pub_5444694740f69928a41e2e38cd6230b56a0cb&q={topic}")
app = Flask(__name__)
@app.route('/')
def get_api():
    response = {'result': r.json()}
    return jsonify(response)

app.run(port=5001)

#pub_5444694740f69928a41e2e38cd6230b56a0cb