# CipherMe.

- This is a Python package in the making for people who enjoy toying around with some of the basic encryption schemes such as Affine Cipher, Vigenere Cipher and Caesar Cipher.

## What is Contained.

The Encryption Algorithms contained herein are:

- Affine Cipher.
- RSA Encryption Algorithm.
- Caesar Cipher.


### Installation.
- To use the package, use pip to install the package:
    `pip install cipherme`

### Usage.
- To use the package, you need to call the methods:
First, you need to import the respective classes from the package:
(i). `AffineCipher` for the Affine Cipher.
(ii). `CaesarCipher` for the Caesar Cipher.

1. For Affine cipher:
    `AffineCipher().encrypt_text(plain_text=None, a=None, b=None)`
    `AffineCipher().decrypt_text(plain_text=None, a=None, b=None)`

2. For Caesar Cipher:
    `CaesarCipher().caesar_encryption(plaintext=None, k=None)`
    `CaesarCipher().caesar_decryption(self, ciphertext=None, k=None)`

### Language Used.

- Python.

### Author.

- Kelyn Paul Njeri.
