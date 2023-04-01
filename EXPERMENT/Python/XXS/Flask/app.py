from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

def detect_xss(url):
    response = requests.get(url)
    if response.status_code == 200:
        body = response.text
        if re.search(r"<\s*script", body) or re.search(r"on\w+=", body):
            if re.search(r"<\s*script\s*alert\(", body):
                return "Reflected XSS with alert() function"
            elif re.search(r"<\s*img\s*src\s*=.*javascript:", body):
                return "Reflected XSS with JavaScript injection in image source"
            elif re.search(r"<\s*a\s*href\s*=.*javascript:", body):
                return "Reflected XSS with JavaScript injection in link"
            elif re.search(r"document\.cookie", body):
                return "Stored XSS with access to cookie"
            else:
                return "Possible XSS vulnerability"
    return "No XSS vulnerability detected"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    url = request.form["url"]
    result = detect_xss(url)
    return render_template("result.html", url=url, result=result)
