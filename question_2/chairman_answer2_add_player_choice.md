import random
print("let's begin now!")
player_choice = input("Press 'enter' to start or press 'q' to quit")
while True:
    random_num = random.randint(1,100)
    try_times = 5
    if player_choice != 'q':
        while try_times > 0:
            if try_times >1:
                input_num = int(input("you have " + str(try_times) +" chances to try,please input your answer."))
                try_times -=1
                if input_num > random_num:
                    print("your answer is too big")
                    continue
                elif input_num < random_num:
                    print("your answer is too small")
                    continue
                elif input_num == random_num:
                    print("Congratulations,you got it!")
                    break
            else:
                input_num = int(input("here is your last chance,please input your answer."))
                if input_num == random_num:
                    print("Congratulations,you got it!")
                    break
                else:
                    print("sorry, you failed,the answer is " + str(random_num))
                    break
        player_choice = input("Press'enter' to go on or press 'q' to quit")
        if player_choice == 'q':
            break
    else:
        break

