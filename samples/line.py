#! /usr/bin/env python
# coding: utf-8

from gchart import gchart

if __name__ == '__main__':

    description = [
        ('year', 'string', 'Year'),
        ('sales', 'number', 'Sales'),
        ('expenses', 'number', 'Expenses')
    ]

    data = [
        ['2004', 1000, 400],
        ['2005', 1170, 460],
        ['2006', 660, 1120],
        ['2007', 1030, 540]
    ]

    options = {
        'title': 'Sales X Expenses',
        'legend': {'position': 'rigth'},
        'hAxis': {'title': 'Ano'},
        'vAxis': {'title': 'Money'}
    }

    gchart.deploy(
        gchart.Line,
        data,
        description=description,
        options=options,
        importjs=True,
        render=True
    )
