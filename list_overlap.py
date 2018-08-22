from __future__ import print_function
x1=raw_input("Enter the elements for list 1 :")
x2=raw_input("Enter the elements for list 2 :")
n=len(x2)
for i in x1 :
	if i in x2:
		print(i,end=" ")