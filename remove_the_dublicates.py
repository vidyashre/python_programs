from __future__ import print_function
list1=raw_input("Enter the elements for list 1   :")
list2=raw_input("Enter the elements for list 2   :")
for i in list1 :
	if i not in list2 :
		print(i,end=" ")
for i in list2 :
	if i not in list1 :
		print(i,end=" ")
