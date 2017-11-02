# -*- coding :utf-8-*-

def func(ls):
    if ls == [] or type(ls) is not list :
        return " "
    for i in range (len(ls)):
        print ((i,ls[i]))
    return "Game Over"

if __name__ == '__main__':
    # ls=[]
    # ls=123
    ls = [10,29,30,41]
    print (func(ls))
