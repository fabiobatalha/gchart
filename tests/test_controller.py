# coding: utf-8

import unittest

from gchart import controller
from xylose.scielodocument import Journal


class ControllerTests(unittest.TestCase):

    def setUp(self):
        from fixtures.journals import accesses, metadata

        self.accesses = accesses

        self.journals = {
            metadata['code'][0]: {
                'metadata': Journal(metadata),
                'accesses': accesses
            }
        }

    def test_journals_list_to_gviz_data(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._journals_list_to_gviz_data(self.journals)

        self.assertEqual(data, [
            ['0034-8910', u'Revista de Saúde Pública', 13982400, 5125575, 632444, 538664, 241622, 20520705]
        ])

    def test_general_source_page_pie_chart_to_gviz_data(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._general_source_page_pie_chart_to_gviz_data(self.accesses)

        expected = [
            [u'fulltext', 5125575],
            [u'abstract', 632444],
            [u'pdf', 919935],
            [u'download', 13982400],
            [u'issues', 73159],
            [u'toc', 538664],
            [u'journal', 241622]
        ]

        self.assertEqual(data, expected)

    def test_general_source_page_pie_chart_to_gviz_data_description(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        description, data = ctrl._general_source_page_pie_chart_to_gviz_data(self.accesses)

        self.assertEqual(
            description,
            [('source', 'string', 'source page'),('accesses', 'string', 'accesses')]
        )


        