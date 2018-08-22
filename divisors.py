from __future__ import print_function
x=range(2,10)
print(x)
n=int(raw_input("Enter a number :"))
print("Divisors of {} is :".format(n))
for i in range(1,100) :
	if n%i==0 :
		print(i, end=' ')