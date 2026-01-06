from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get("https://example.com")
    return {
        "message": "Supply chain demo",
        "status_code": r.status_code
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
