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
        self.options(**options)
        self._importjs = importjs

        if isinstance(data, str):
            self._jsondata = data
            self._jsondatasource = 'url'
        else:
            data_table = DataTable(description)
            data_table.LoadData(data)
            self._jsondata = data_table.ToJSon()
            self._jsondatasource = 'given'

    @property
    def _data(self):

        data = {
            'options': self.optionstojs,
            'importjs': self._importjs,
            'jsondata': self._jsondata,
            'jsondatasource': self._jsondatasource
        }

        return data

    def data_table_response(self, reqId=0):

        return u'google.visualization.Query.setResponse({"status": "ok", "table": %s, "reqId": %s});' % (self._jsoncode, reqId)

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
