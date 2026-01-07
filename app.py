import sqlite3
import subprocess
import base64

# VULNERABILITY 1: Hardcoded Secret
API_KEY = "SK-88221-ALPHA-BETA-GAMA"

def get_user_data(username):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    
    # VULNERABILITY 2: SQL Injection (String Formatting)
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchone()

def execute_payload(payload):
    # VULNERABILITY 3: Command Injection
    # Using shell=True with user input is dangerous
    subprocess.run(payload, shell=True)

def parse_input(data):
    # VULNERABILITY 4: Use of eval()
    # eval is dangerous as it can execute arbitrary code
    return eval(data)

if __name__ == "__main__":
    print("App is running...")