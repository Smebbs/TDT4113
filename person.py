class Person:

    def __init__(self):
        self.key = ''
        self.cipher = None
        self.encoded = ''

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_encoded(self, encoded):
        self.encoded = encoded

    def get_encoded(self):
        return self.encoded

    def set_cipher(self, cipher):
        self.cipher = cipher

    def get_cipher(self):
        return self.cipher
