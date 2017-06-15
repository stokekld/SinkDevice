from flask import Flask

service = Flask(__name__)
service.config.from_object('config')

import register
import user
import frontend
