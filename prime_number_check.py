n=int(raw_input("Enter the number :"))
count=0
for i in range(1,(n+1)//2) :
	if n % i == 0 :
		count+=1
print(count)
if count==1 :
	print("{} is a prime number".format(n))
else:
	print("{} is not a prime number".format(n))
	