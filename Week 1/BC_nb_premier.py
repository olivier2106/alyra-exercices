# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:47:49 2019

@author: Olivier
"""

def nb_premier_check(num):
    # Python program to check if the input number is prime or not

    #num = input("Nombre premier please")
    
    # take input from the user
    # num = int(input("Enter a number: "))
    
    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")
       
def indicatrice_Euler(p,q):
    return (p - 1)(q - 1) 

     
def algoRSA(num1,num2):
    if ((num1 % i) == 0) and ((num1 % i) == 0):
        
        n=num1*num2
        