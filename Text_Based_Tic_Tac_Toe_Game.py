import random
win=str()
def check(bb):
	global win
	bolo=False
	for i in [0,3,6]:
		if(bb[i]=="X" or bb[i]=="O"):
			if (bb[i]==bb[i+1] and bb[i+1]==bb[i+2]):
				if bb[i]=="X":
					win="X"
					return True
				else:
					win="O"
					return True
	for i in [0,1,2]:
		if(bb[i]=="X" or bb[i]=="O"):
			if(bb[i]==bb[i+3] and bb[i+3]==bb[i+6]):
				if bb[i]=="X":
					win="X"
					return True
				else:
					win="O"
					return True
	if (bb[0]=="O" or bb[0]=="X"):
		if (bb[0]==bb[4] and bb[4]==bb[8]):
			if bb[0]=="X":
				win="X"
				return True
			else:
				win="O"
				return True
	if (bb[2]=="X" or bb[2]=="O"):
		if (bb[2]==bb[4] and bb[4]==bb[6]):
			if bb[2]=="X":
				win="X"
				return True
			else:
				win="O"
				return False

	return False
def Tic_Tac_Toe():
	print("Welcome to Tic Tack Toe. Player is X, Computer is O. This is a new game. Board numbers are as follows:")
	for i in [1,4,7]:
		print("\t"+str(i)+" "+"|"+" "+str(i+1)+" "+"|"+" "+str(i+2))
	user_ip=list()
	cmp_ip=list()
	board=list()
	choice=[1,2,3,4,5,6,7,8,9]
	for i in range(9):
		board.append(" ")
	iter=True
	count=0
	con_st=True
	while(iter):
		user_ip.append(input("Enter your desired location[1-9] : "))
		choice.remove(user_ip[len(user_ip)-1])
		board[user_ip[len(user_ip)-1]-1]="X"
		for i in [0,3,6]:
                        print("\t"+board[i]+" "+"|"+" "+board[i+1]+" "+"|"+" "+board[i+2])
		if check(board):
			if win=="X":
				status=str(input("You have won!Wanna Play Again(y/n)?"))
				if(status=="y" or status=="Y"):
					return True
				else:
					print("Thank You")
					return False
			else:
				status=str(input("Computer has won!Wanna Play Again(y/n)?"))
				if(status=="y" or status=="Y"):
					return True
				else:
					print("Thank You")
					return False
		###################################################################################################
		cmp_ip.append(random.choice(choice))
                choice.remove(cmp_ip[len(cmp_ip)-1])
                print("The computer picked :"+str(cmp_ip[len(cmp_ip)-1]))
                board[cmp_ip[len(cmp_ip)-1]-1]="O"
                #print("Board:\n")
                for i in [0,3,6]:
                        print("\t"+board[i]+" "+"|"+" "+board[i+1]+" "+"|"+" "+board[i+2])
		
		if check(board):
                        if win=="X":
                                status=str(input("You have won!Wanna Play Again(y/n)?"))
                                if(status=="y" or status=="Y"):
                                        return True
                                else:
                                        print("Thank You")
                                        return False
                        else:
                                status=str(input("Computer has won!Wanna Play Again(y/n)?"))
                                if(status=="y" or status=="Y"):
                                        return True
                                else:
                                        print("Thank You")
                                        return False

      		count=count+1
		if count==4 :
			status=str(input("It's a Draw!wanna play again(y/n)?"))
			if (status=="y" or status=="Y"):
				return True
			else:
				print("Thank You")
				return False
while(Tic_Tac_Toe()):
	print("*"*20)
