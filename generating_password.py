import random
s="asdfghjklzxcvbnmqwertyuiop1234567890!@#$%^&*()<>?,./:ASDFGHJKLQWERTYUIOPZXCVBNM"
n=8
password="".join(random.sample(s,n))
print password