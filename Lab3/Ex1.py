# Use the cryptography library to code and decode a message
# Name: Anthony Liao


from cryptography.fernet import Fernet
import cryptography

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"This is a really secret message!")
# instead of f string, we use b"" to indicate byte strings
print(f"Encoded text: {encoded_text}")

decoded_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")

# print ("Cryptography library version:", cryptography.__version__)
# This program checks and prints the version of the cryptography library

