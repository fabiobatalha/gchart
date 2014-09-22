# coding: utf-8

import unittest
import copy

from gchart import controller
from xylose.scielodocument import Journal


class ControllerTests(unittest.TestCase):

    def setUp(self):
        from fixtures.journals import accesses, metadata

        self.accesses = copy.deepcopy(accesses)
        self.metadata = copy.deepcopy(metadata)

        self.journals = {
            metadata['code'][0]: {
                'metadata': Journal(self.metadata),
                'accesses': self.accesses
            }
        }

    def test_journals_list_to_gviz_data(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._journals_list_to_gviz_data(self.journals)

        self.assertEqual(data, [
            ['0034-8910', u'Revista de Saúde Pública', 13982400, 5125575, 632444, 538664, 241622, 20520705]
        ])

    def test_general_article_year_month_lines_chart_to_gviz_data(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._general_article_year_month_lines_chart_to_gviz_data(self.accesses)

        expected = [
            ['Jan', 0, 308695, 328228, 396586],
            ['Feb', 0, 369071, 432585, 608402],
            ['Mar', 0, 700404, 760372, 883628],
            ['Apr', 0, 741216, 426252, 959445],
            ['May', 0, 840924, 657833, 1017929],
            ['Jun', 0, 600715, 640475, 760328],
            ['Jul', 0, 387179, 405063, 891044],
            ['Aug', 0, 559773, 631494, 0],
            ['Sep', 0, 626891, 784848, 0],
            ['Oct', 0, 708194, 865038, 0],
            ['Nov', 0, 641054, 1031974, 0],
            ['Dec', 4593, 334299, 435887, 0]
        ]

        self.assertEqual(data, expected)

    def test_general_article_year_month_lines_chart_to_gviz_description(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._general_article_year_month_lines_chart_to_gviz_data(self.accesses)

        expected = [
            ('months', 'string', 'months'),
            (u'2011', 'number'),
            (u'2012', 'number'),
            (u'2013', 'number'),
            (u'2014', 'number')
        ]

        self.assertEqual(description, expected)

    def test_general_source_page_pie_chart_to_gviz_data(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._general_source_page_pie_chart_to_gviz_data(self.accesses)

        expected = [
            [u'html', 5125575],
            [u'abstract', 632444],
            [u'pdf', 13982400],
            [u'issues', 73159],
            [u'toc', 538664],
            [u'journal', 241622]
        ]

        self.assertEqual(sorted(data), sorted(expected))

    def test_general_source_page_pie_chart_to_gviz_data_description(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._general_source_page_pie_chart_to_gviz_data(self.accesses)

        expected = [
            ('source', 'string', 'source page'),
            ('accesses', 'number', 'accesses')
        ]

        self.assertEqual(
            description,
            expected
        )
