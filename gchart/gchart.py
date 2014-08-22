# coding: utf-8

import os
import webbrowser
import json
import uuid
import base64

from mako.template import Template
from mako.lookup import TemplateLookup

from gviz_api import DataTable

templates = '%s/../templates' % os.path.dirname(__file__)

mylookup = TemplateLookup(
    directories=[templates],
    output_encoding='utf-8',
    encoding_errors='replace'
)


def deploy(mode, description, data, options, importjs=False, render=False):

    obj = mode(description, data, options, importjs=importjs)

    if render:
        obj.render()
    else:
        return str(obj)


class GChart(object):

    _allowed_options = ['title', 'legend', 'width', 'heigth']

    def __init__(self, description, data, options, importjs=False):
        self._options = {'width': 500, 'height': 500}
        self._id = base64.b64encode(str(uuid.uuid4()), altchars=['_', '_'])
        self.options(**options)
        data_table = DataTable(description)
        data_table.LoadData(data)
        self._importjs = importjs
        self._jscode = data_table.ToJSCode(self._id)

    @property
    def _data(self):

        data = {
            'jscode': self._jscode,
            'options': self.optionstojs,
            'id': self._id,
            'importjs': self._importjs
        }

        return data

    @property
    def optionstojs(self):
        return 'var options = %s' % json.dumps(self._options)

    def options(self, **kwargs):

        for attrib, value in kwargs.items():
            if attrib in self._allowed_options:
                self._options[attrib] = value
            else:
                raise TypeError('option %s unknow' % attrib)

    def render(self):
        path = os.path.abspath('/tmp/%s' % uuid.uuid4())

        with open(path, 'w') as f:
            mytemplate = mylookup.get_template(self.tpl)
            f.write(mytemplate.render(**self._data))

        webbrowser.open('file://%s' % path)

    def __str__(self):
        mytemplate = mylookup.get_template(self.tpl)
        return mytemplate.render(**self._data)


class Pie(GChart):

    _allowed_options = ['title', 'legend', 'width', 'heigth', 'is3D', 'pieHole', 'pieSliceText', 'pieStartAngle']
    tpl = 'pie.tpl'


class Line(GChart):

    _allowed_options = ['title', 'legend', 'width', 'heigth', 'series', 'hAxis', 'vAxis', 'domainAxis', 'curveType']
    tpl = 'line.tpl'
