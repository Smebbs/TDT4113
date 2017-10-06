from cipher import *
from random import randint
from caesar import *


# Read the text file to find keys
lines = tuple(open("english_words.txt", 'r'))


class Unbreakable(Cipher):
	def __init__(self):
		self.caesar = Caesar()
		super().__init__()

	# Caesar, but the key changes
	def encode(self, text, key):
		encoded = ""
		n = 0
		for char in text:
			if n > len(key) - 1:
				n = 0
			encoded += self.caesar.encode(char, ord(key[n]))
			n += 1
		return encoded

	# Decode same as Caesar, with key change
	def decode(self, text, key):
		decoded = ""
		n = 0
		for char in text:
			if n > len(key) - 1:
				n = 0
			decoded += self.caesar.decode(char, ord(key[n]))
			n += 1
		return decoded

	# Gets a random word and uses this as a key
	def generate_keys(self):
		return lines[randint(0, len(lines) - 1)]
