from hacker import *
from sender import *
from receiver import *

def main():
	# Test Caesar
	caesar = Caesar()
	print("Caesar match? ", caesar.verify("TEST", 20))
	print("----------------------------------------------------------------------------------------------")

	# Test Multiplication
	mult = Multiplication()
	print("Multiplication match? ", mult.verify("TEST", mult.generate_keys()))
	print("----------------------------------------------------------------------------------------------")

	# Test Affine
	affine = Affine()
	print("Affine match? ", affine.verify("TEST", affine.generate_keys()))
	print("----------------------------------------------------------------------------------------------")

	# Test Unbreakable
	unbreakable = Unbreakable()
	print("Unbreakable match? ", unbreakable.verify("TEST", unbreakable.generate_keys()))
	print("----------------------------------------------------------------------------------------------")

	# Test RSA
	rsa = RSA()
	n, d = rsa.generate_keys()
	e = rsa.get_e()
	encoded = rsa.encode("TEST", (n, e))
	decoded = rsa.decode(encoded, (n, d))
	print("RSA match? ", "TEST" == decoded)
	print("----------------------------------------------------------------------------------------------")

	# Test Sender & Receiver
	secret = "zoroaster"
	cipher = Affine()
	key = cipher.generate_keys()

	sender = Sender()
	sender.set_key(key)
	sender.set_cipher(affine)
	sender.encode_message(secret)
	print("Sending secret message. This is what will be sent: ", sender.get_encoded())

	receiver = Receiver()
	receiver.set_key(key)
	receiver.set_cipher(affine)
	receiver.decode_message(sender.get_encoded())
	print("Message received. This is the decoded message: ", receiver.get_decoded())

	print("----------------------------------------------------------------------------------------------")

	# Test Hacker
	hacker = Hacker()
	caesar = Caesar()
	mult = Multiplication()
	affine = Affine()
	unbreakable = Unbreakable()
	rsa = RSA()

	cyphers = [caesar, mult, affine, unbreakable, rsa]

	for i in range(0, 5):
		message = unbreakable.generate_keys().strip()
		print("Original message:", message)
		cypher = cyphers[i]
		encoded = cypher.encode(message, cypher.generate_keys())
		hacker.hack(encoded, cypher)
		print("----------------------------------------------------------------------------------------------")



if __name__ == "__main__":
	main()