from flask import Flask, render_template, request
import requests, os

# Post URL - if not exist in config map will take local host
url_post = os.environ.get('POST_URL', 'http://127.0.0.1:5001/post')
# Defualt API - Defualt value to send post request.
def_api = os.environ.get('DEFUALT_API', 'https://api.chucknorris.io/jokes/random')
# Response - Empty init value
response = ""

app = Flask(__name__)

@app.route('/', methods=['GET'])
def render():
    return render_template('index.html', def_api=def_api)

@app.route('/', methods=['POST'])
def post():
    try:
        if request.method == 'POST':
            url = request.form['url']
            post_response = requests.post(url_post, json=url)
            post_response_json = post_response.json()
            print("from front",post_response_json)
            return render_template('index.html', response=post_response_json)
    except:
        response="Please provide correct URL!"
        return render_template('index.html', response=response)

    return render_template('index.html')


@app.route('/uselessfact', methods=['POST', 'GET'])
def uselessfact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    post_response = requests.post(url_post, json=url)
    post_response_json = post_response.json()
    post_response_split = post_response_json['text']
    print("from front",post_response_split)
    return render_template('index.html', response=post_response_split)

@app.route('/funnyfact', methods=['POST', 'GET'])
def funnyfact():
    url = "https://api.chucknorris.io/jokes/random"
    post_response = requests.post(url_post, json=url)
    post_response_json = post_response.json()
    post_response_split = post_response_json['value']
    print("from front",post_response_split)
    return render_template('index.html', response=post_response_split)





# Health check
@app.route('/ready')
def health():
    return 'Im Ready :)', 200


if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
