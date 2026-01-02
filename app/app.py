import os

def get_user(user_id):
    query = "SELECT * FROM users WHERE id=" + user_id

    return query

def connect():
    password = os.environ.get("DB_PASSWORD")


if __name__ == "__main__":
    connect()
    get_user("123")
