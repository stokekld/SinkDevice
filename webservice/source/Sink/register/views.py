from datetime import datetime
from flask import request, send_file, Response, render_template
from Sink.app import service
from xlsxwriter import Workbook
import os

from .models import db

# @service.route('/', methods=['GET'])
# def index():
    # return render_template('index.html')

@service.route('/', methods=['GET'])
def principal():
    return render_template('get_reg.html')

@service.route('/register', methods=['GET'])
def setRegister():
    if request.args.get('data'):
        db.register.insert({
            'data': request.args.get('data'),
            'date': datetime.now()
        })
    return Response()

@service.route('/getRegisters', methods=['GET'])
def getRegister():

    file = 'registers.xlsx'
    path = os.path.join(service.config['BASEDIR'], file)

    workbook = Workbook(path)
    worksheet = workbook.add_worksheet()

    registers = db.register.find()

    for index, register in enumerate(registers):
        worksheet.write('A' + str( index + 1), register['data'])
        worksheet.write('B' + str( index + 1), str(register['date']))

    workbook.close()

    return send_file(path, attachment_filename=file, as_attachment=True);
