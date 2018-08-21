def party_planar(cookies,people):
	leftcookies=None
	leftpeople=None

	try :
		leftcookies=cookies//people
		leftpeople=cookies%people
	except ZeroDivisionError:
	     print("OOps ,you enetered 0 people will be attending.")
	     print("Please enter a good number of peple for a party.")

	return(leftcookies,leftpeople)