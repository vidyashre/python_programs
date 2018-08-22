from __future__ import print_function
string =raw_input("Enter the string   :").split(" ")

n=len(string)

for i in range(1,n):
	print(string[n-i],end=" ")
print(string[0])