import random
import itertools
#no_sides=int(input("Enter no.of sides:  "))
xi=input("Enter min and max as #min max: ")
min=int(xi[0])
max=int(xi[2])
def Roll_It():
	for i in itertools.repeat(1):
		print("You have "+str(random.randint(min,max)))
		check=input("Do yow want to roll again(y/n) ")
		if(check=='y' or check=='Y'):
			continue
		else:
			break
	print("\t\tThank_You\t\t");
Roll_It()
