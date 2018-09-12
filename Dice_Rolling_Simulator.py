import random
import itertools
no_sides=int(input("Enter no.of sides:\t"))
min,max=int(input("Enter min and max separated by comma as min_val,max_val"))
def Roll_It():
	for i in itertools.repeat(1):
		print("You have "+random.randint(min,max+1)+"\n")
		check=char(input("Do yow want to roll again(y/n)"))
		if(check=='y' or check=='Y'):
			continue
		else:
			break
Roll_It()
