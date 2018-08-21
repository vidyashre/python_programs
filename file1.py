result = eval(raw_input("Enter an expression: "))
print(result)
names=raw_input("Enter the names separated by , :  ").title().split(",")
ages=raw_input("Enter the ages separated by ,").split(",")
message="Your name is {} and age is {}"
for name, age in zip(names , ages) :
	print(message.format(name, age))