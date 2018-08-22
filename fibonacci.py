from __future__ import print_function
n=int(raw_input("Enter the number till where we have to find the fibonacci numbers     :"))
n1=0
n2=1
sum=0
print("Fibonacci series of {} number is   :".format(n))
if n==1 :
	print(n1)
elif n==2 :
	print("{} {}".format(n1,n2))
else :
	print("{} {}".format(n1,n2),end=' ')
	for i in range(3,n+1) :
		sum=eval('n1+n2')
		print(sum,end=" ")
		n1=n2
		n2=sum


