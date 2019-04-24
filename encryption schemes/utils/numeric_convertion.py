"""
    Module: Numeric Convention.
    Author: Kelyn Paul Njeri.
    Date: 24th April 2019
"""


class NumericOperation():
    def text_to_numerics(self, plain_text=None):
        for i, letter in enumerate(plain_text):
            if i < len(plain_text):
                if i is 0:
                    numeral = ord(letter) - 65
                else:
                    numeral = ord(letter) - 97

                return numeral

    def numerics_to_text(self, numerics=None):
        pass

    def check_co_prime(self, a=None, b=None):
        pass
