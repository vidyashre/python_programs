from __future__ import print_function
import random
cow=0
bull=0

print("Gerated 4 digit random number is ")
random_number=random.randint(1000,9999)
print(random_number)
guesser_number=raw_input("Guess a 4 digit number ")
print(guesser_number)
n=guesser_number
while random_number!=0:
	r=random_number%10
	g=int(guesser_number)%10
	random_number=random_number/10
	guesser_number=int(guesser_number)/10
	if r == g :
		cow+=1
	else:
		bull+=1
print("\ncow count is ",cow)
print("\nbull count is ",bull)
if cow==len(n):
	print("\nYour guess is correct")
