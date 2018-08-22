from __future__ import print_function
import random
choice="yes"
list1=[]
list2=[]
print("Enter the elements for list1")
while choice=="yes" :
		list1.append(random.randint(1,100))
		print(list1)
		choice=raw_input("Do you want to continue ?(yes/no) :")


choice="yes"
print("Enter the elements for list2")
while choice=="yes" :
		list2.append(random.randint(1,100))
		print(list2)
		choice=raw_input("Do you want to continue ?(yes/no) :")
print("Common elements between the list1 and list2 are   :")
for i in list1 :
	if i in list2 :
		print(i)

