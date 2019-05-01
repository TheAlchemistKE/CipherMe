class NumberOperations():
    def __init__(self):
        """Class Constructor."""
        self.letter_numeric_values = []
        self.cipher_text = []

    def text_to_number(self, plain_text=None):
        """Responsible for converting the letters of a word into a list of its equivalent numeric values."""
        for i, letter in enumerate(plain_text):
            if i < len(plain_text):
                if i is 0:
                    numeral = ord(letter) - 65
                else:
                    numeral = ord(letter) - 97
                self.letter_numeric_values.append(numeral)
        return self.letter_numeric_values

    def numerics_to_text(self, numeric_cipher=None):
        """Responsible for converting the numeric values of a word back into the original word."""
        for k, numeral in enumerate(numeric_cipher):
            if k < len(numeric_cipher):
                if k is 0:
                    numeral += 65
                else:
                    numeral += 97
                letter = chr(numeral)
                self.cipher_text.append(letter)
        return ''.join(self.cipher_text)

    def multiplicative_inverse(self, a=None, m=None):
        """Modular Inverse"""
        m0 = m
        y = 0
        x = 1

        if (m == 1):
            return 0

        while (a > 1):
            # q is quotient
            q = a // m

            t = m

            # m is remainder now, process
            # same as Euclid's algo
            m = a % m
            a = t
            t = y

            # Update x and y
            y = x - q * y
            x = t

        # Make x positive
        if (x < 0):
            x = x + m0

        return x

def __gcd(a=None, b=None):
    # Everything divides 0
    if (a == 0 or b == 0):
        return 0

    # base case
    if (a == b):
        return a

    # a is greater
    if (a > b):
        return __gcd(a - b, b)

    return __gcd(a, b - a)

# Function to check and print if
# two numbers are co-prime or not
def check_coprime(a=None, b=None):

    if (__gcd(a, b) == 1):
        return True
    else:
        return False
