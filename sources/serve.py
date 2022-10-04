from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def calculate():
    return subprocess.check_output(['python', 'sources/calculate.py', 100, 200])
