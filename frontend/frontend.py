from flask import Flask, render_template, request
import requests, os


url_post = os.environ.get('POST_URL', 'https://ofekbb/post')
# url_post = 'https://ofekbb/post'

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        url = request.form['url']
        post_response = requests.post(url_post, json={url})
        post_response_json = post_response.json()
        print("from front",post_response_json)
        return f'Resonse: {post_response_json}!'

    return render_template('index.html')


if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
