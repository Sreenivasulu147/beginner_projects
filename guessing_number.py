import random
while True:
    number_to_guess=random.randint(1,100)
    try:
        user_input =int(input('guess number 1 to 100:='))
    except ValueError:
        print('please give valid number')
    else:
        print(number_to_guess)
        if user_input > number_to_guess:
            print('Number is too low')
        elif user_input < number_to_guess:
            print('number is high')
        elif number_to_guess==user_input:
            print('well done')

#generate random number
#ask the user to make guess
#if not a valid number
#print an error
#if number <guess
#print too low
#if num>guess
#print too hig
#else print well done