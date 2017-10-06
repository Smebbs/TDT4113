from cipher import *
import random
from crypto_utils import modular_inverse


class Multiplication(Cipher):

	def __init__(self):
		super().__init__()



	def encode(self, msg, key):
		encoded = ""
		for char in msg:
			# Similar to Caesar, but multiplies the key, instead of adding it.
			index = (ord(char) * key - 32) % 95
			encoded += Cipher.alphabet[index]
		return encoded


	def decode(self, msg, key):
		decoded = ""
		inverse = modular_inverse(key, 95)
		for char in msg:
			# Finds the modular inverse, and multiplies with this.
			index = (ord(char) * inverse - 32) % 95
			decoded += Cipher.alphabet[index]
		return decoded


	# Tests if a random number is a viable key. If it isn't, find another one.
	def generate_keys(self):
		n = random.randint(1, 999)
		while True:
			inverse = modular_inverse(n, 95)
			if not inverse:
				n = random.randint(1, 999)
			else:
				return n

