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

from flask import Flask, Response

app = Flask(__name__)

@app.route('/services')
def services():
    return [
        {'name': 'test1'},
        {'name': 'test'}
    ]


@app.route('/<string:service_name>/status')
def status(service_name):
    return {'status': 'stopped'}

