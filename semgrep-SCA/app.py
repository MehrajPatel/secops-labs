import requests
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'super-secret'

@app.route('/')
def index():
    # This uses a vulnerable version of Flask session handling
    session['user'] = 'admin'
    
    # This uses a version of requests vulnerable to specific header leaks
    resp = requests.get("https://httpbin.org/get")
    return resp.text

if __name__ == "__main__":
    app.run()