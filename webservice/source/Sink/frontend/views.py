from flask import render_template
from Sink.app import service

@service.route('/', methods=['GET'])
def index():
    return render_template('index.html')
