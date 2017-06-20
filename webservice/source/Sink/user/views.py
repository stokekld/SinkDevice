from flask import redirect, url_for, request
from Sink.app import service
import md5

from .models import db

@service.route('/auth', methods=['POST'])
def authorization():
    credentials = request.form
    device = db.device.find_one()

    if device["user"] == credentials["user"] and device["password"] == md5.new(credentials["password"]).hexdigest():
        return redirect(url_for('principal'))
    else:
        return redirect(url_for('index'))
