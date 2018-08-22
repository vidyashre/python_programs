import random
guesser=0
count=0
random_number=random.randint(1,100)
print(random_number)
while guesser!=random_number and guesser!=exit :
	guesser=raw_input("Enter the number :")
	if guesser=="exit" :
		break
	elif int(guesser) < random_number :
		print("Your guess is too low")
		count+=1
	elif int(guesser) > random_number :
		print("Your guess is too high")
		count+=1
	else:
		print("Your guess is correct and you took {} tries".format(count))
		count=0
        