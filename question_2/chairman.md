import random
random_num = random.randint(1,5)
print("let's begin now!")
try_times = 5
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
            print("sorry, you failed")
            break


