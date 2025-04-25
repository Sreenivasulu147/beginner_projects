#take input from the user
#create computer choices
#if computer choice and paper choice is true
#taid else you win
import random
choices=('r','s','p')
while(True):
    user_choice=input('r,s,p enter your choice among them:=')
    if user_choice not in choices:
        print('invalid choice please choose again')
        break
    computer_choice=random.choice(choices)
    if computer_choice==user_choice:
        print('tai')
    elif ((user_choice=='r' and computer_choice=='s')
          or (user_choice=='s' and computer_choice=='p')
          or (user_choice=='p' and computer_choice=='r')):
        print('win 😘😘😘👌👌👌👌👌👌 you win')
    else:
        print('you lose')