"""
    Module Name: Caesar Cipher.
    Author: Kelyn Paul Njeri.
    Module Description: 
    - This module deals with the encryption of plain text into cipher text using the Caesar cipher.
    - This module deals with the decryption of cipher text to plain text with a know shift key.
"""
from .utils.number_operations import NumberOperations


class CaesarCipher():
    """ 
        Deals with encryption and decryption of plain text and vice versa.

        It does not take in any parameters. However, it has two local variables 
        self.caesar_encrypted_values -> This contains the letters of the encrypted plain text.
        self.caesar_decrypted_values -> This contains the letters of the decrypted plain text.
    """

    def __init__(self):
        self.number_ops = NumberOperations()
        self.caesar_encrypted_values = []
        self.caesar_decrypted_values = []

    def caesar_encryption(self, plaintext=None, k=None):
        """
            Deals with the convertion of plain text into cipher text using Caesar Cipher.
            Parameters: 
            plaintext -> This is text to be encrypted.
            k -> This is the shift key.
        """
        numeric_values = self.number_ops.text_to_number(plain_text=plaintext)

        # Looping through the list of text numerals to apply Caesar Cipher.
        for index, numeral in enumerate(numeric_values):
            if index <= len(numeric_values):
                # c = (x + k) mod 26
                encrypted_value = (numeral + k) % 26
                self.caesar_encrypted_values.append(encrypted_value)
        return self.number_ops.numerics_to_text(numeric_cipher=self.caesar_encrypted_values)

    def caesar_decryption(self, ciphertext=None, k=None):
        """
            Deals with the convertion of cipher text into plain text using Caesar Cipher.
            Parameters: 
            ciphertext -> This is text to be encrypted.
            k -> This is the shift key.
        """
        numeric_values = self.number_ops.text_to_number(plain_text=ciphertext)

        # Looping through the list of text numerals to apply Caesar Cipher for decryption.
        for index, numeral in enumerate(numeric_values):
            if index <= len(numeric_values):
                # x = (c - k) mod 26
                decrypted_value = (numeral - k) % 26
                self.caesar_decrypted_values.append(decrypted_value)
        return self.number_ops.numerics_to_text(numeric_cipher=self.caesar_decrypted_values)
