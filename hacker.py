from person import *
from caesar import *
from multiplication import *
from affine import *
from unbreakable import *
from rsa import *
from cipher import *
from crypto_utils import *


class Hacker(Person):
	def __init__(self):
		self.words = tuple(open("english_words.txt", 'r'))
		super().__init__()

	def hack(self, text, cipher):
		self.cipher = cipher
		if isinstance(cipher, Caesar):
			self.caesar_hack(text)
		elif isinstance(cipher, Multiplication):
			self.multiplicative_hack(text)
		elif isinstance(cipher, Affine):
			self.affine_hack(text)
		elif isinstance(cipher, Unbreakable):
			self.unbreakable_hack(text)
		elif isinstance(cipher, RSA):
			print("RSA detected.")
			print("I can't hack RSA, sorry.")
		else:
			pass

	def caesar_hack(self, text):
		print("Caesar detected.")
		for key in range(1, 95):
			decoded = self.cipher.decode(text, key)
			if self.is_real_word(decoded):
				print("Caesar hack finished. Was the word? ", decoded)
				return
		print("Caesar hack failed.")

	def multiplicative_hack(self, text):
		print("Multiplicative detected.")
		for key in range(1, 999):
			decoded = self.cipher.decode(text, key)
			if self.is_real_word(decoded):
				print("Multiplicative hack finished. Was the word? ", decoded)
				return
		print("Multiplicative hack failed.")

	def affine_hack(self, text):
		print("Affine detected.")
		for mult_key in range(1, 999):
			for caesar_key in range(1, 95):
				decoded = self.cipher.decode(text, (mult_key, caesar_key))
				if self.is_real_word(decoded):
					print("Affine hack finished. Was the word? ", decoded)
					return
		print("Affine hack failed.")

	def unbreakable_hack(self, text):
		print("Unbreakable detected.")
		for key in self.words:
			decoded = self.cipher.decode(text, key)
			if self.is_real_word(decoded):
				print("Unbreakable hack finished. Was the word? ", decoded)
				return
		print("Unbreakable hack failed.")

	def is_real_word(self, word):
		return word + "\n" in self.words
