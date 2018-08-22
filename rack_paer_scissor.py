import sys
def compare(u1,u2):
	if u1==u2 :
		return "Game is tie up"
	elif u1=="rock":
		if u2=="scissor" :
			return "Rock wins"
		else :
			return "paper wins"
	elif u1=="scissor" :
		if u2=="paper" :
			return "scissor wins"
		else :
			return "Rock wins"
	elif u1=="paper" :
		if u2=="rock" :
			return "paper wins"
		else :
			return "scissor wins"
	else :
		print("You have enetered wrong input")
	sys.exit()

user1=raw_input("Enter your name :")
user2=raw_input("And your name :")
user1_answer=raw_input("{}, What you are going to choose rock,paper or scissor  :".format(user1))
user2_answer=raw_input("{}, What you are going to choose rock,paper or scissor  :".format(user2))
print(compare(user1_answer,user2_answer))