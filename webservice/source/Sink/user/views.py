from flask import Response
from Sink.app import service

from .models import db

@service.route('/auth', methods=['POST'])
def principal():
    device = db.device.find_one()
    print device
    return Response()
