#!/usr/bin/env python

#
# This python file represents a mtr server
# It utilizes websockets stream as transport
#

from flask import Flask, send_from_directory
from flask_sockets import Sockets

import json
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)
sockets = Sockets(app)

#@sockets.route('/mtr')
@sockets.route('/')
def mtr_socket(ws):
    request = json.loads(ws.receive())
    print 'received', request
    args = ['./mtr', '-p', '-c', '300']
    if request.get('no_dns'):
        args.append('--no-dns')
    if request.get('protocol') == 'TCP':
        args.append('-T')
    elif request.get('protocol') == 'UDP':
        args.append('-u')
    if request.get('version') == '4':
        args.append('-4')
    elif request.get('version') == '6':
        args.append('-6')
    args.append(request.get('hostname'))
    mtr = Popen(args, stdout=PIPE, stderr=STDOUT)
    for line in mtr.stdout:
        try:
            data = [x if i == 1 else float(x) for (i, x) in enumerate(line.split())]
            data[2] = "%.2f%%" % (data[2] / 1000.)
        except ValueError:
            # probably an error from stderr
            data = line
        finally:
            try:
                ws.send(json.dumps(data))
            except:
                mtr.terminate()
                print 'disconnected'

if __name__ == '__main__'
    app.run()

    application = app
