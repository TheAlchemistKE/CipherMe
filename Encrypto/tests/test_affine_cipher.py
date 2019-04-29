from .base_test import TestBaseCase as base


class TestAffineCipher(base):
    def setUp(self):
        base.setUp(self)

    def test_plain_text_to_cipher_text(self):
        self.assertEqual(self.affine.encrypt_text(
            plain_text='Kelyn', a=7, b=15), 'Hrobc')

    def test_cipher_text_to_plain_text(self):
        pass

    def tearDown(self):
        base.tearDown(self)
