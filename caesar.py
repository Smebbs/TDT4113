from cipher import *
import random


class Caesar(Cipher):

	def __init__(self):
		super().__init__()



	def encode(self, msg, key):
		encoded = ""
		for char in msg:
			# Takes the ascii value of the char minus 32, since our alphabet starts at ascii char 32.
			# Adds the key, to encode, and takes mod 95 to ensure we stay within the 95 chars.
			index = (ord(char) + key - 32) % 95
			encoded += Cipher.alphabet[index]
		return encoded


	def decode(self, msg, key):
		decoded = ""
		for char in msg:
			# Similar to encode, but this time subtract the key.
			index = (ord(char) - key - 32) % 95
			decoded += Cipher.alphabet[index]
		return decoded


	def generate_keys(self):
		# Don't return zero, that would not function as a key.
		return random.randint(1, 95)