from .utils.number_operations import NumberOperations, check_coprime
"""
    Module Name: Affine Cipher
    Author: Kelyn Paul Njeri.
    Module Description: This module applies the Affine Cipher to the plain text entered.
"""


class AffineCipher():
    """Deals with encryption and decryption using the Affine Cipher.
        It does not take in any parameters. However, it has two local variables 
        self.encryption_list -> This contains the letters of the encrypted plain text
        self.decryption_list -> This contains the letters of the decrypted plain text
    """

    def __init__(self):
        self.number_ops = NumberOperations()
        self.encryption_list = []
        self.decryption_list = []

    def encrypt_text(self, plain_text=None, a=None, b=None):
        """
            Converts the plain text entered into cipher text.
            Functional Parameters: 
            -> plain_text = This is the plain text that is supposed to be converted to cipher text.
            -> a = the first key.
            -> b = the second key.
        """
        # Converting plain_text to a list of numerals.
        numeral_values = self.number_ops.text_to_number(plain_text = plain_text)
        
        # Checking co-primitivity.
        if check_coprime(a = a, b = b) is True:
            # Looping through to encrypt every single letter of the plain text.
            for index, numeral in enumerate(numeral_values):
                if index <= len(numeral_values):
                    # Formula: E(x) = (ax + b) mod 26
                    encrypted_value = ((a * numeral) + b) % 26
                    self.encryption_list.append(encrypted_value)
            return self.number_ops.numerics_to_text(numeric_cipher=self.encryption_list)

        else:
            return "'a' and 'b' are not co-prime."

    def decrypt_text(self, cipher_text=None, a=None, b=None):
        """
            Converts the cipher text entered into plain text when the encryption keys are known.
            Functional Parameters: 
            -> cipher_text = This is the cipher text that is supposed to be converted to plain text.
            -> a = the first key.
            -> b = the second key.
        """
        numeral_values = self.number_ops.text_to_number(plain_text = cipher_text)
        # Looping through to decrypt every single letter of the cipher text.
        for index, number in enumerate(numeral_values):
            if index <= len(numeral_values):
                multiplicative_inv = self.number_ops.multiplicative_inverse(
                    a=a, m=26)
                # x = ((a^-1 * c) - b) mod 26
                decrypted_value = (multiplicative_inv * (number - b)) % 26
                self.decryption_list.append(decrypted_value)
        return self.number_ops.numerics_to_text(numeric_cipher=self.decryption_list)
                

