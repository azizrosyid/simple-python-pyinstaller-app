from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def calculate():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    cmd = f"python sources/add2vals.py {num1} {num2}"
    result = subprocess.check_output(cmd, shell=True)
    return result

