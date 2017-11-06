系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

    import random

    key = random.randint(1,100)

    def play_game(num):
        num = int(num)

        if num > key:
            return 1
        elif num < key:
            return -1
        else:
            return 0

    if __name__ == "__main__":
        count = 5
        
        while count >0:
            num = input('please input your number(1-100):')
            ret = play_game(num)
            if ret == 0:
                print("you got it!")
                break
            elif ret == 1:
                print("larger than key")
            else:
                print("small than key")

            count = count - 1
        print("the answer is ", key)