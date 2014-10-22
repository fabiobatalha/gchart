# coding: utf-8

import os
import webbrowser
import json
import uuid
import random

from mako.template import Template
from mako.lookup import TemplateLookup

from gviz_api import DataTable

templates = '%s/../templates' % os.path.dirname(__file__)

mylookup = TemplateLookup(
    directories=[templates],
    output_encoding='utf-8',
    encoding_errors='replace'
)


def deploy(mode, data, description=None, options=None, importjs=False, render=False):

    options = options or {}
    description = description or []
    data = data or []

    obj = mode(data, description, options, importjs=importjs)

    if render:
        obj.render()
    else:
        return str(obj)


class GChart(object):

    _allowed_options = ['title', 'legend', 'width', 'heigth']

    def __init__(self, data, description, options, importjs=False):
        self._options = {'width': 500, 'height': 500}
        self.options(**options)
        self._importjs = importjs
        self._description = description
        self._dat = data
        if isinstance(data, str) or isinstance(data, unicode):
            self._jsondata = data
            self._jsondatasource = 'url'
        else:
            data_table = DataTable(self._description)
            data_table.LoadData(data)
            self._jsondata = data_table.ToJSon()
            self._jsondatasource = 'given'

    @property
    def _data(self):

        data = {
            'options': self.optionstojs,
            'importjs': self._importjs,
            'jsondata': self._jsondata,
            'jsondatasource': self._jsondatasource,
            'id': random.randrange(255)
        }

        return data

    def data_table_response(self, req_id=0):
        data_table = DataTable(self._description)
        data_table.LoadData(self._dat)
        return data_table.ToJSonResponse(req_id=req_id)

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

    _allowed_options = ['title', 'legend', 'width', 'heigth', 'series', 'hAxis', 'vAxis', 'domainAxis', 'curveType', 'pointSize']
    tpl = 'line.tpl'


class List(GChart):

    _allowed_options = ['title', 'legend', 'width', 'heigth', 'alternatingRowStyle', 'allowHtml', 'page', 'pageSize', 'showRowNumber', 'sortColumn', 'sortAscending']
    tpl = 'list.tpl'
