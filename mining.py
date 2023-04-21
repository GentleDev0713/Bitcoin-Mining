# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:18:17 2023

@author: Administrator
"""

import sys
import hashlib
import re
import string
from itertools import product
import time

def VariantMine(hash, value):
    alphabet = list(string.ascii_letters)
    result = ""
    x = re.findall("[^a-zA-Z]", value)

    indexes = []
    for v in x:
        index = value.index(v)
        value = value[:index] + 'a' + value[index+1::]
        indexes.append(index)
    
    length = len(indexes)
    for i in product(alphabet, repeat = length):  
        comb = list(i)
        for j in range(length):
            value = value[:indexes[j]] + comb[j] + value[indexes[j]+1::]
        if hash == hashlib.sha256(value.encode('utf-8')).hexdigest():
            result = value
            break
            
    return result

def check(value):
    if len(value) != 16:
        print("Value must be 16 characters.Input Again.")
        GenerateHash() 

def GenerateHash():
    print("--------------------------------------")
    origin = input("Enter your value: ")
    check(origin)
    origin_hash = hashlib.sha256(origin.encode('utf-8')).hexdigest()
    print(origin_hash)
    main()

def Mining():
    print("--------------------------------------")    

    origin_hash = input("Enter your Hash value: ")        

    redacted = input("Enter a redacted value: ")
    
    st = time.time()
    result = VariantMine(origin_hash, redacted)
    et = time.time()
    
    elapsed_time = (et-st) * 1000
    if result == "":
        result = "No Result."
    
    print('Execution time:', int(elapsed_time), 'milliseconds')
    print("Result : "+result)
    main()

def main():
    print("-------------Select Mode--------------")
    print("1. Generate the Hash value")
    print("2. Mining")
    print("3. Exit")
    
    select = input("Enter Number: ")

    if select == "1":
        GenerateHash()
    elif select == "2":
        Mining()
    else:
        sys.exit(0)
            

if __name__ == '__main__':
    main()




