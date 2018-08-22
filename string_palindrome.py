def reverse(word):
	x=''
	for i in range(len(word)) :
		x+=word[len(word)-1-i]
	return x

name=raw_input("Enter the string:")
reversed_string=reverse(name)
print(reversed_string)
if reversed_string == name :
	print("Strings are palindrome")
else:
	print("Strings are not palindrome")

