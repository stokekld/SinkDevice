from flask import redirect, url_for, request
from Sink.app import service

from .models import db

@service.route('/auth', methods=['POST'])
def principal():
    # device = db.device.find_one()
    # print device
    print request.form
    return redirect(url_for('index'))
