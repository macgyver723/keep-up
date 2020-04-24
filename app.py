from flask import Flask, request, jsonify, render_template, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "not implemented"