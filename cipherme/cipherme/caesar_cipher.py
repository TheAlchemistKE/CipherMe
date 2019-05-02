from .utils.number_operations import NumberOperations


class CaesarCipher():
    def __init__(self):
        self.number_ops = NumberOperations()
        self.caesar_encrypted_values = []
        self.caesar_decrypted_values = []

    def caesar_encryption(self, plaintext=None, k=None):
        numeric_values = self.number_ops.text_to_number(plain_text=plaintext)

        for index, numeral in enumerate(numeric_values):
            if index <= len(numeric_values):
                # c = (x + k) mod 26
                encrypted_value = (numeral + k) % 26
                self.caesar_encrypted_values.append(encrypted_value)
        return self.number_ops.numerics_to_text(numeric_cipher=self.caesar_encrypted_values)

    def caesar_decryption(self, ciphertext=None, k=None):
        numeric_values = self.number_ops.text_to_number(plain_text=ciphertext)

        for index, numeral in enumerate(numeric_values):
            if index <= len(numeric_values):
                # x = (c - k) mod 26
                decrypted_value = (numeral - k) % 26
                self.caesar_decrypted_values.append(decrypted_value)
        return self.number_ops.numerics_to_text(numeric_cipher=self.caesar_decrypted_values)
