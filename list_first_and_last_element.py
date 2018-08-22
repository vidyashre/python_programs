def first_and_last_element(arr) :
	return [arr[0],arr.pop()]

list_element=raw_input("Enter the list elements  :").split(' ')
output_list=first_and_last_element(list_element)
print(output_list)
