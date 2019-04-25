"""
    Module: Affine Cipher.
    Author: Kelyn Paul Njeri.
    Date: 24th April 2019
"""

from .utils.numeric_convertion import NumericOperation

_number_ops = NumericOperation()

class AffineCipher():
   
    def text_encryption(self, a=None, b=None, plain_text=None):
        # Check that 'a' and 'b' are co-prime.
        _number_ops.check_co_prime(a=a, b=b)
        # Convert the letters in the plain_text into their respective numeric values.
        _number_ops.text_to_numerics(plain_text=plain_text)
        # Convert the numeric values into their encrypted values using the formula E(x) = (ax + b) mod 26.
        

        # Map the converted numeric values back into letters.
        _number_ops.numerics_to_text()
        # Return the encrypted text.
        pass