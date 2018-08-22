import random
x=[2,8,6,9]#(raw_input("Enter the list of elements :"))
print x
for i in x:
	print i
output=[i for i in x if i % 2 == 0]
print(output)


print("Using random functions :")
list_elements=[]
num_list=random.randint(1,10)
print(num_list)
while len(list_elements) < num_list :
	list_elements.append(random.randint(10,100))
print(list_elements)

even_list=[i for i in list_elements if i % 2 == 0]
print(even_list)



