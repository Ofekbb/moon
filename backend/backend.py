from flask import Flask, request
import requests


app = Flask(__name__)

# Define a simple API endpoint
@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    get = requests.get(data)
    get_json= get.json()
    print("from back GET",get_json)
    return get_json

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True,port=5001)

