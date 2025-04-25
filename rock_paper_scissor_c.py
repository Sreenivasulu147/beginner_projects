import random
def game_start():
    choices=('r','s','p')
    user_choice=input('enter your choice r,s,p: ')
    computer_choice=random.choice(choices)
    if user_choice not in choices:
        print('choose valid choice.. run agian')
        quit()
    return user_choice,computer_choice
def play_game():
    user_choice, computer_choice=game_start()
    if computer_choice==user_choice:
        print('tie')
    elif ((user_choice=='r' and computer_choice=='s')
          or (user_choice=='s' and computer_choice=='p')
          or (user_choice=='p' and computer_choice=='r')):
        print(''' yayooo... you win''')
    else:
        print('you lose>>☆*: .｡. o(≧▽≦)o .｡.:*☆')

while True:
    user=input('you want to continue this game y/n')
    if user.lower()=='y':
        play_game()
    else:
        print('thank you for playing see you again....y')
        exit()

