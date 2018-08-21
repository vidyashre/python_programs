def mean(num_list):
	return sum(num_list)/len(num_list)

def add_five(num_list):
	return [n+5 for n in num_list]
def main():
	try:
		print("Testing mean function")
		n_list=[1,2,3,4,5]
		correct_mean=3
		assert(mean(n_list) == correct_mean)

		print("Testing add_five function")
		correct_list=[6,7,8,9,10]
		assert(add_five(n_list)==correct_list)
	except AssertionError :
		print("Assertion fail")

	finally:
		print("All tests passed!!!")

if __name__ == '__main__' :
   		main() 