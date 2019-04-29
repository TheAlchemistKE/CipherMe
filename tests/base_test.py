import unittest


class TestBaseCase(unittest.TestCase):
    def setUp(self):
        self.text_example_list = [
            'Kelyn Paul', 'New Orleans', 'Cry Me a River.^^@8#)E#Y', 'Password@123']

    def tearDown(self):
        self.text_example_list = None
