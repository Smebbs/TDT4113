from cipher import *
import random
from crypto_utils import modular_inverse
from multiplication import *
from caesar import *


class Affine(Cipher):

	def __init__(self):
		super().__init__()
		self.caesar = Caesar()
		self.mult = Multiplication()


	def encode(self, msg, key):
		# Combine the mult and caesar to encode the msg.
		key0, key1 = key
		encoded = self.caesar.encode(self.mult.encode(msg, key0), key1)
		return encoded


	def decode(self, msg, key):
		# Combine the mult and caesar to decode the msg.
		key0, key1 = key
		decoded = self.mult.decode(self.caesar.decode(msg, key1), key0)
		return decoded


	def generate_keys(self):
		key1 = random.randint(1, 999)
		while True:
			inverse = modular_inverse(key1, 95)
			if not inverse:
				key1 = random.randint(1, 999)
			else:
				break
		key2 = random.randint(1, 95)
		return (key1, key2)