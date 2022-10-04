from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def calculate():
    cmd = 'python sources/add2vals.py 200 200'
    result = subprocess.check_output(cmd, shell=True)
    return result

