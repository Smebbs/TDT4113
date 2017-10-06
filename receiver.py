from person import Person


class Receiver(Person):

    def __init__(self):
        super().__init__()
        self.decoded = ''

    def get_decoded(self):
        return self.decoded

    def set_decoded(self, decoded):
        self.decoded = decoded

    def decode_message(self, msg):
        self.set_decoded(self.cipher.decode(msg, self.key))