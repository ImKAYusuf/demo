def palindrome(word):
	if word==word[::-1]:
		return True
	else:
		return False 
word=input('Enter a word to check palindrome: ') 
if palindrome(word):
	print(f"The given word '{word}' is panindromw")
else:
	prnt(f"The given word '{word}' is not a palindrome")
