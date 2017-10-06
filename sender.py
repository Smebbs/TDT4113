from person import Person
#from rsa import RSA


class Sender(Person):

    def __init__(self):
        super().__init__()

    def encode_message(self, msg):
        self.set_encoded(self.cipher.encode(msg, self.key))