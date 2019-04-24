"""
    Module: Affine Encryption Tests.
    Author: Kelyn Paul Njeri.
    Date: 24th April 2019
"""
from .base_test import TestBaseCase as base


class TestAffineCipher(base):
    """
        Description: This module tests the efficiency and correctness of the code written for the Affine cipher. This module also makes sure that the code returns what is expected and gives assurance to the developer that everything works as it should.
    """
    def setUp(self):
        base.setUp(self)

    def tearDown(self):
        base.tearDown(self)
