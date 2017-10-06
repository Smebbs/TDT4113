from cipher import *
from crypto_utils import modular_inverse
from crypto_utils import generate_random_prime
from crypto_utils import blocks_from_text
from crypto_utils import text_from_blocks

from random import randint


class RSA(Cipher):
	def __init__(self):
		super(Cipher, self).__init__()
		self.n = None
		self.e = None

	def encode(self, text, key):
		n, e = key
		blocks = blocks_from_text(text, 3)
		encoded_block = []
		for b in blocks:
			encoded_block.append(pow(b, e, n))
		return encoded_block

	def decode(self, blocks, key):
		n, d = key
		decoded_block = []
		for b in blocks:
			decoded_block.append(pow(b, d, n))
		return text_from_blocks(decoded_block, 16)

	def generate_keys(self):
		p = generate_random_prime(16)
		q = generate_random_prime(16)
		while p == q:
			q = generate_random_prime(16)
		n = p * q
		o = (p - 1) * (q - 1)
		e = randint(3, o - 1)
		d = modular_inverse(e, o)

		while d == False:
			p = generate_random_prime(16)
			q = generate_random_prime(16)
			while p == q:
				q = generate_random_prime(16)
			n = p * q
			o = (p - 1) * (q - 1)
			e = randint(3, o - 1)
			d = modular_inverse(e, o)
		self.set_keys((n, e))
		return n, d

	def set_keys(self, key):
		self.n, self.e = key

	def get_n(self):
		return self.n

	def get_e(self):
		return self.e
