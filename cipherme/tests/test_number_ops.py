from .base_test import TestBaseCase as base


class TestNumberOperations(base):
    def setUp(self):
        base.setUp(self)

    def test_text_to_number_convertion(self):
        self.assertEqual(self.num_ops.text_to_number(
            plain_text=self.text_example0), self.numeric_example0)

    def test_number_to_text_convertion(self):
        self.assertEqual(self.num_ops.numerics_to_text(
            numeric_cipher=self.numeric_example0), self.text_example0)
