# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:18:25 2019

@author: Olivier
"""
import panda as pd

def caesar_original():
    #get the sentence to encrypt
    phrase=input("phrase à chiffrer")
    i=0
    phrase_encrypted=[]
    while i < len(phrase):
        phrase_encrypted.append(chr(ord(phrase[i])+1))
        i+=1
    print(''.join(phrase_encrypted))
    
    
def occurence_in_text():
    #get the sentence to encrypt
    phrase=input("phrase à chiffrer")
    #unique letter in variable no space
    letters=''.join(list(set(phrase)))
    #df_result=pd.DataFrame()
    
    for i in letters:
        #on compte les duplicate
        print(i,phrase.count(i))

def vigenere():
    #get the sentence to encrypt
    phrase=input("phrase à chiffrer")
    i=0
    phrase_encrypted=[]
    while i < len(phrase):
        temp_modulo=i%3
        phrase_encrypted.append(chr(ord(phrase[i])+temp_modulo))
        i+=1
    print(''.join(phrase_encrypted))
    
def vigenere_decrypt():
    #get the sentence to encrypt
    phrase=input("phrase à dechiffrer")
    i=0
    phrase_decrypted=[]
    while i < len(phrase):
        temp_modulo=i%3
        phrase_decrypted.append(chr(ord(phrase[i])-temp_modulo))
        i+=1
    print(''.join(phrase_decrypted))
    
def regroupement(n):
    phrase=input("phrase à dechiffrer")
    #remove space
    phrase = phrase.replace(' ', '')
    #on refait comme avec vigenere mais en gardant que les multiples de 0
    i=0
    phrase_encrypted=[]
    while i < len(phrase):
        if i%3==0:
            phrase_encrypted.append(chr(ord(phrase[i])))
        i+=1
    print(''.join(phrase_encrypted))
    
    
def caesar():
    #get the sentence to encrypt
    phrase=input("phrase à chiffrer")
    i=0
    phrase_encrypted=[]
    while i < 10:
        phrase_encrypted.append(ord(phrase[i]))
        i+=1
    print(phrase_encrypted.replace(",", ""))
    
    