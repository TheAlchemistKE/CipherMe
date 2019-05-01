from .base_test import TestBaseCase as base


class TestCaesarCipher(base):
    def setUp(self):
        base.setUp(self)

    def test_caesar_encryption(self):
        self.assertEqual(self.caesar.caesar_encryption(
            plaintext='Kelyn', k=7), 'Rlsfu')

    def test_caesar_decryption(self):
        self.assertEqual(self.caesar.caesar_decryption(
            ciphertext='Rlsfu', k=7), 'Kelyn')

    def tearDown(self):
        base.tearDown(self)
