# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 11:52:25 2019

@author: Olivier
"""

def ChangeHex(n):
    

    #j initialise mon remainder
    c = ""
    
    #je modul par 16
    x = (n % 16)
    
    #je calcule mon remainder
    if (x < 10):
        c = x
    if (x == 10):
        c = "A"
    if (x == 11):
        c = "B"
    if (x == 12):
        c = "C"
    if (x == 13):
        c = "D"
    if (x == 14):
        c = "E"
    if (x == 15):
        c = "F"

    #j aggrege till it s over
    #ici big
    if (n - x != 0):
        return ChangeHex(n / 16) + str(c)
    else:
        return str(c)


import numpy as np
import pandas as pd

def ChangeHex(n,hexa_big):
    
       
    if (n < 0):
        hexa_big.append(str(0))
        return hexa_big
    elif (n<=1):
        hexa_big.append(str(n))
        return hexa_big
    else:
        x =(n%16)
        if (x < 10):
            hexa_big.append(str(x)), 
        if (x == 10):
            hexa_big.append("A"),
        if (x == 11):
            hexa_big.append("B"),
        if (x == 12):
            hexa_big.append("C"),
        if (x == 13):
            hexa_big.append("D"),
        if (x == 14):
            hexa_big.append("E"),
        if (x == 15):
            hexa_big.append ("F"),
        return ChangeHex( np.int(n / 16),hexa_big )
   

def hexa_big(n):
    hexa_big=ChangeHex(n,[])
    print(''.join(hexa_big))
    
def ChangeHex_little(n,hexa_big):
    
       
    if (n < 0):
        hexa_big.appendleft(str(0))
        return hexa_big
    elif (n<=1):
        hexa_big.appendleft(str(n))
        return hexa_big
    else:
        x =(n%16)
        if (x < 10):
            hexa_big.appendleft(str(x)), 
        if (x == 10):
            hexa_big.appendleft("A"),
        if (x == 11):
            hexa_big.appendleft("B"),
        if (x == 12):
            hexa_big.appendleft("C"),
        if (x == 13):
            hexa_big.appendleft("D"),
        if (x == 14):
            hexa_big.appendleft("E"),
        if (x == 15):
            hexa_big.appendleft ("F"),
        return ChangeHex_little( np.int(n / 16),hexa_big )
   

def hexa_little(n):
    hexa_little=ChangeHex(n,[])
    print(''.join(hexa_little))
    
  

def ChangeHex(n):
    hexa_output=[]
    #hexa_little=
    #hexa_big=
    if (n < 0):
        hexa_output.append(0)
        hexa_output=''.join(hexa_output)
    elif (n<=1):
        hexa_output.append(n)
        hexa_output=''.join(hexa_output)
    else:
        x =(n%16)
        if (x < 10):
            hexa_output.append(x), 
        if (x == 10):
            hexa_output.append("A"),
        if (x == 11):
            hexa_output.append("B"),
        if (x == 12):
            hexa_output.append("C"),
        if (x == 13):
            hexa_output.append("D"),
        if (x == 14):
            hexa_output.append("E"),
        if (x == 15):
            hexa_output.append("F"),
        hexa_output=''.join(hexa_output)
        ChangeHex( np.int(n / 16) )