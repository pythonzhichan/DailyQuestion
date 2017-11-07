import random
number = random.randint(1,100)
times = 0
running = True
while running:
    guess =int(input('Please enter an integer between 1 and 100 : '))
    if guess == number:
        print('Congratulations, you guessed it .')
        break
    elif guess < number:
        times+=1
        if times == 5:
            running = False
        else:
            print('No, it is a little hegher than that.')       
    else:
        times+=1
        if times == 5:
            running = False
        else:
            print('No,it is a little lower than that.')     
else:
    print('The game is over, answer is', number)

