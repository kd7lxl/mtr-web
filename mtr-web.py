#!/usr/bin/env python
#
# mtr-web - a WebSockets-based frontend for mtr
# Copyright (C) 2015 Tom Hayward <tom@tomh.us>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, send_from_directory
from flask_sockets import Sockets

import json
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/mtr')
def mtr_socket(ws):
    request = json.loads(ws.receive())
    print 'received', request
    args = ['mtr', '-p', '-c', '300']
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
            data = [x if i == 1 else int(x) for (i, x) in enumerate(line.split())]
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


@app.route('/')
def index():
    return send_from_directory('', 'index.html')


if __name__ == '__main__':
    app.run()

application = app
