#! /usr/bin/env python
# coding: utf-8

from gchart import gchart

if __name__ == '__main__':

    description = {
        "company": ("string", "Company"),
        "salary": ("number", "Salary"),
    }

    data = [
        {"company": "Mike", "salary": (10000, "$10,000")},
        {"company": "Jim", "salary": (800, "$800")},
        {"company": "Alice", "salary": (12500, "$12,500")},
        {"company": "Bob", "salary": (7000, "$7,000")}
    ]

    options = {
        'title': 'cucueueuxc',
        'is3D': False,
        'pieHole': 0.4,
        'pieSliceText': 'label',
        'pieStartAngle': 100,
        'legend': {'position': 'rigth'}
    }

    gchart.deploy(
        gchart.Pie,
        description,
        data,
        options,
        importjs=True,
        render=True
    )
