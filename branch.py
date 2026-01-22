word=input("Enter a word to check palindrome: ")
if word==word[::-1]:
	print("The given word is palindrome")
else:
	print("The given word is not a palindrome")
