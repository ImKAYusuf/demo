def palindrome(word):
	if word==word[::-1]:
		return True
	else:
		return False 
word=input('Enter a word to check palindrome: ') 
print(f"{palindrome(word)}")
