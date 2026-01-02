import os

API_KEY = os.environ.get("API_KEY")

def connect():
    password = os.environ.get("DB_PASSWORD")
    print("Connecting securely")

if __name__ == "__main__":
    connect()

