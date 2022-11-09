# gwaliorws: This file is part of gwalior, a web service to control
# other web services.
#
# Copyright (C) 2022  Sumanth Vepa.
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
from flask import Flask, Response
from markupsafe import escape

app = Flask(__name__)

_services = {
    'test1': {
        'status': 'stopped'
    },
    'test2': {
        'status': 'stopped'
    },
    'flaky': {
        'status': 'stopped'
    }
}


@app.route('/services')
def services():
    return [
        {'service_name': service_name}
        for service_name in _services.keys()
    ]


@app.route('/<string:service_name>/status')
def status(service_name):
    service_name = escape(service_name)
    if service_name in _services.keys():
        return {
            'status': _services.get(service_name).get('status')
        }
    return '', 404


@app.route('/<string:service_name>/start')
def start(service_name):
    service_name = escape(service_name)
    if service_name in _services.keys():
        if service_name == 'flaky':
            return Response(
                response=json.dumps({
                    'error_code': 1,
                    'error_message': 'Unable to start the web service',
                    'error_detail': 'It is dummy service that will '
                                    + 'fail to start by design'
                }),
                status=500,
                mimetype='application/json')
        _services[service_name]['status'] = 'running'
        return '', 200
    return '', 404


@app.route('/<string:service_name>/stop')
def stop(service_name):
    service_name = escape(service_name)
    if service_name in _services.keys():
        if service_name == 'flaky':
            return Response(
                response=json.dumps({
                    'error_code': 1,
                    'error_message': 'Unable to stop the web service',
                    'error_detail': 'It is dummy service that will '
                                    + 'fail to stop by design'
                }),
                status=500,
                mimetype='application/json')
        _services[service_name]['status'] = 'stopped'
        return '', 200
    return '', 404
