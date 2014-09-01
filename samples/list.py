#! /usr/bin/env python
# coding: utf-8

from gchart import gchart

if __name__ == '__main__':

    description = [
        ("company", "string", "Person"),
        ("salary", "number", "Salary"),
    ]

    data = [
        ["Mike", (10000, "$10,000")],
        ["Jim", (800, "$800")],
        ["Alice", (12500, "$12,500")],
        ["Bob", (7000, "$7,000")]
    ]

    options = {'showRowNumber': True}

    gchart.deploy(
        gchart.List,
        description,
        data,
        options,
        importjs=True,
        render=True
    )
