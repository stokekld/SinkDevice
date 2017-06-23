from flask import Flask
import os

service = Flask(__name__)
service.secret_key = os.urandom(24)
service.config.from_object('config')

import register
import user
import frontend
