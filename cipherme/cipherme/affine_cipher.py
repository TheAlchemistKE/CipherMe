from .utils.number_operations import NumberOperations, check_coprime


class AffineCipher():
    """Deals with encryption and decryption using the Affine Cipher."""

    def __init__(self):
        self.number_ops = NumberOperations()
        self.encryption_list = []
        self.decryption_list = []

    def encrypt_text(self, plain_text=None, a=None, b=None):
        """Converts the plain text entered into cipher text."""
        numeral_values = self.number_ops.text_to_number(plain_text=plain_text)
        if check_coprime(a=a, b=b) is True:
            for index, numeral in enumerate(numeral_values):
                if index <= len(numeral_values):
                    # E(x) = (ax + b) mod 26
                    encrypted_value = ((a * numeral) + b) % 26
                    self.encryption_list.append(encrypted_value)
            return self.number_ops.numerics_to_text(numeric_cipher=self.encryption_list)

        else:
            return "'a' and 'b' are not co-prime."

    def decrypt_text(self, cipher_text=None, a=None, b=None):
        numeral_values = self.number_ops.text_to_number(plain_text=cipher_text)
        for index, number in enumerate(numeral_values):
            if index <= len(numeral_values):
                multiplicative_inv = self.number_ops.multiplicative_inverse(
                    a=a, m=26)
                # x = ((a^-1 * c) - b) mod 26
                decrypted_value = (multiplicative_inv * (number - b)) % 26
                self.decryption_list.append(decrypted_value)
        return self.number_ops.numerics_to_text(numeric_cipher=self.decryption_list)
                

