def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
if __name__=="__main__":
    n=3
    print('�����������{}�εĻ���'.format(n))
    while True:
        if n>0:
            number=input('������Ҫ���������쳲�������:')
            if number<1:
                n-=1
                print ('�����������С��1�����������1������,�㻹ʣ��%s�λ�����'%n)
            else:
                for i in range(1,number+1):
                    print fib(i),
                print '\n'
        else:
            break
    print ('��Ϸ����')
