# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:30:30 2019

@author: Olivier
"""

#Cible = CiblePrécédente x (bloc[Actuel].date - 
#block[Actuel-2016].date) /
#(deux semaines en secondes)

def cible(cible,block_actuel):
    cible=cible*()
    
    

#Difficulté actuelle =cible(max)/cible(actuelle) 
    
import numpy as np 
  
def difficulte(cible):
    cible_max=((2**16) - 1) * (2**208)
    cible_current= cible
    return cible_max/cible_current

import binascii

def readjustment_block(block_number):
    return block_number%2016==0

def hextoint(hex_value):
    return int.from_bytes(hex_value, byteorder="big",signed="False")

def reverse_endian(byte_string):
    if byte_string[0:2]=="0x":
        byte_string=byte_string[2:]
        
    print(byte_string)
    
    temp=bytearray.fromhex(byte_string)
    temp.reverse()
    return temp

def difficulte_from_byte(byte_string):
    #transform byte string in little endian to big endian
    temp=reverse_endian(byte_string)
    print(temp)
    #transform my big endian to int
    temp2=hextoint(temp)
    #calculate difficulté
    temp3=difficulte(temp2)
    return temp3

print(difficulte_from_byte("0x1c0ae493"))

def nb_bitcoin_per_block(nb_block) :
    return 50/(nb_block//210000)**2

def nb_of_bitcoin_in_circulation(nb_block) :
    #variable
    nb_steps=int(nb_block//210000)
    block_in_new_step=nb_block-nb_steps*210000
    #init
    total_number=0
    #calculate the full step
    for i in range(nb_steps):
        total_number= total_number+(50/(2**i))*210000
    #add the remainder
    total_number=total_number+block_in_new_step*(50/(2**(nb_steps+1)))
    return total_number

from datetime import datetime

def date_to_block():
    then = datetime(2009, 1, 1, 1, 1, 1)        # Random date in the past
    now  = datetime(2100, 1, 1, 1, 1, 1)                         # Now
    duration = now - then                         # For build-in functions
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60*10)[0]
    return minutes

def time_to_block():
    #detemine nb of blocks based on time delta
    nb_block=date_to_block()
    return nb_of_bitcoin_in_circulation(nb_block), nb_bitcoin_per_block(nb_block)


    



import struct
val = 0x11223344
val = struct.unpack("<I", struct.pack(">I", val))[0]
print( "%08x" % val)



   

