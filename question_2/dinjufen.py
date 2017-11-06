from random import randint

count = 0                               
num = randint(1, 100)                   
print('*'*10, " Welcome to the Guess Game ", '*'*10)
while count < 5:                        
    print("You still have %d chance(s)"%(5-count))
    try:                                
        guess = int(input("Please input your number between 1 and 100:"))
        if 1 <= guess <= 100:           
            if guess < num:             
                print("Too small, try again~")
            elif guess > num:           
                print("Too big, try again~")
            else:                       
                print("Just right!")    
                break                   
        else:                           
            print("Input out of range!")
    except ValueError:                  
        print("Wrong input!")           
    count += 1                          
    
if count >= 5:                          
    print("The right number is: %d"%num)       
