from ..cipherme.affine_cipher import AffineCipher
from ..cipherme.caesar_cipher import CaesarCipher
from ..cipherme.utils.number_operations import NumberOperations
import unittest


class TestBaseCase(unittest.TestCase):
    def setUp(self):
        """Setting Up the Tests."""
        self.num_ops = NumberOperations()
        self.affine = AffineCipher()
        self.caesar = CaesarCipher()
        # Text Test Values.
        self.text_example0 = 'Kelyn'
        self.text_example1 = 'This is a car'
        self.text_example2 = 'Password@123...'

        # Numeric Test Values.
        self.numeric_example0 = [10, 4, 11, 24, 13]
        self.numeric_example1 = []
        self.numeric_example2 = []

    def tearDown(self):
        self.num_ops = None
        # Text Test Values.
        self.text_example0 = None
        self.text_example1 = None
        self.text_example2 = None

        # Numeric Test Values.
        self.numeric_example0 = None
        self.numeric_example1 = None
        self.numeric_example2 = None
