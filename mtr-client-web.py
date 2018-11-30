from flask import Flask, send_from_directory
from flask_sockets import Sockets

import json
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)
sockets = Sockets(app)

@app.route('/')
def index():
    return send_from_directory('', 'index.alt.html')


if __name__ == '__main__':
    app.run()

application = app
