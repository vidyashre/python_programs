from __future__ import print_function
list_of_elements=raw_input("Enter the number :")

print (list_of_elements)
n=raw_input("Enter the limit :")
#output_list=[x for x in list_of_elements if x<n]
for i in list_of_elements:
	if i <n :
		print(i,end=' ')
#print(output_list)
