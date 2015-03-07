import unittest
import slowpoetryserver as server


class SlowPoetryTests(unittest.TestCase):
    def setUp(self):
        self.argument_parser=server.create_parser()
    def test_argumentParserIsSetupCorrectly(self):
        self.assertTrue(self.argument_parser.usage!="")