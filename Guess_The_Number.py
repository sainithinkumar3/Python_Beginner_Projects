import random
pick = random.randint(0,9)*random.randint(0,9)
def Guess_The_Number():
	guess=int(input("Guess it: (Hint: Lies between 0-100)"))
	diff=abs(pick-guess)
	print(diff)
	if(diff>=1 and diff<=10):
		print("Almost There")
		return False
	elif(diff>=10 and diff<=20):
		print("not so far")
		return False
	elif(diff==0):
		print("WOW! That's Correct")
		return True
	elif(diff>=20 and diff<=40):
		print("That's far")
		return False
	elif(diff>=40):
		print("Too Far");
		return False
	else:
		pass
	return False
while(not(Guess_The_Number())):
	pass
