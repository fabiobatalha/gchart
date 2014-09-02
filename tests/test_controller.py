# coding: utf-8

import unittest

from gchart import controller
from xylose.scielodocument import Journal


class ControllerTests(unittest.TestCase):

    def setUp(self):
        from fixtures.journals import accesses, metadata

        self.journals = {
            metadata['code'][0]: {
                'metadata': Journal(metadata),
                'accesses': accesses
            }
        }

    def test_journals_list_to_gviz_data(self):

        ctrl = controller.Ratchet('fakeratchetapiclient')

        result = ctrl._journals_list_to_gviz_data(self.journals)

        self.assertEqual(result, [
            ['0034-8910', u'Revista de Saúde Pública', 13982400, 5125575, 632444, 538664, 241622, 20520705]
        ])
