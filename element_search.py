from __future__ import print_function
list_elements=raw_input("Enter the list  :").split(" ")

x=raw_input("Enter the number  :")
if x in list_elements :
	print("Element searched")
else:
	print("Element not searched")