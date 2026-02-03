# 5. Ask for a sentence from the user (using input()). Turn the sentence into a list of strings.
# Reverse the list.  Join the reversed list back into a string.
# Name: Anthony Liao
# Date: Feb 3, 2026

sentence = input("Enter a sentence: ")

# 1. Turn the string into a listo f words
word = sentence.split(" ")
print("List of words:", word)

# 2. Reverse the list
word.reverse()
print("Reversed list of words:", word)

# 3. Join the reversed list back into a string
reversed_sentence = " ".join(word)
print("Reversed sentence:", reversed_sentence)