#!/usr/bin/env python
# coding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="gchart",
    version='0.1b',
    description="Wrapper para construção de gráficos e tabelas utilizando o Google Charts.",
    author="SciELO",
    author_email="scielo-dev@googlegroups.com",
    license="BSD 2-clause",
    url="http://docs.scielo.org",
    packages=['gchart'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Topic :: System",
        "Topic :: Utilities",
    ],
    setup_requires=["nose>=1.0", "coverage"],
    test_suite="nose.collector"
)
