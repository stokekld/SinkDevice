from datetime import datetime
from flask import request, send_file, Response
from Sink.app import service
from xlsxwriter import Workbook
import os

from .models import db

@service.route('/register', methods=['POST'])
def setRegister():
    if 'data' in request.form:
        db.register.insert({
            'data': request.form['data'],
            'date': datetime.now()
        })
    return Response()

@service.route('/register', methods=['GET'])
def getRegister():

    file = 'registers.xlsx'
    path = os.path.join(service.config['BASEDIR'], file)

    workbook = Workbook(path)
    worksheet = workbook.add_worksheet()

    registers = db.register.find()

    for index, register in enumerate(registers):
        worksheet.write('A' + str( index + 1), register['data'])
        worksheet.write('B' + str( index + 1), register['date'])

    workbook.close()

    return send_file(path, attachment_filename=file, as_attachment=True);
