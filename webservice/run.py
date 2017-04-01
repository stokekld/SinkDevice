from Sink.app import service

service.run(host=service.config['HOST'], port=service.config['PORT'], debug=service.config['DEBUG'])

