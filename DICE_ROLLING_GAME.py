#LOOP
import random
while True:
    choice=input('roll dice y/n')
    if choice=='y' or choice=='Y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'{die1},{die2}')
    elif choice=='n':
        print('Thanks for playing')
    else:
        print('invalid choice!')

#GENERATE RANDAM NUMBERS
#PRINT THEM
#IF USER ENTERS N
#PRINT THANK YOU MESSAGE
#TERMINATE
#ELSE
#PRINT VALID CHOICE