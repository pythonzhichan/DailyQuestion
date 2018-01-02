#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jason Zhang
#
# Created:     01/01/2018
# Copyright:   (c) Jason Zhang 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#Q4
#using matrix multiplication to resolve Fibonacci number calculation

import numpy as np

def fibonacci_number(n):
    fib_matrix = np.matrix([[1,1],[1,0]])**(n-1)*np.matrix([[1],[0]])
    return fib_matrix[0,0]

#program starts here
invalid_input = True
while invalid_input:
    try:
        n = int(input("Please enter an integer: "))
        print("The xth fibonacci number is :",fibonacci_number(n))
        invalid_input = False
    except ValueError:
        print("Please enter an integer")



