from operator import length_hint, mod
import hashlib
import colorama
from hashlib import *
colorama.init(autoreset=True)
moon = '''\033[1;35m
       o                     __...__     *               
              *   .--'    __.=-.             o
     |          ./     .-'     
    -O-        /      /   
     |        /    '"/               *
             |     (@)     
            |        \                         .
            |         \
 *          |       ___\                  |
             |  .   /  `                 -O-
              \  `~~\                     |
         o     \     \            *         
                `\    `-.__           .  
    .             `--._    `--'jgs
                       `---~~`                *
            *                   o
 ___         _                              _____            _ 
|   \  __ _ | |_   _ __   __ _  _ _        |_   _| ___  ___ | |
| |) |/ _` ||   \ | '  \ / _` || ' \         | |  / _ \/ _ \| |
|___/ \__/_||_||_||_|_|_|\__/_||_||_|        |_|  \___/\___/|_|   
'''
print(moon)
print("\033[1;33m=====================================================")
print("\033[1;31m1] - \033[1;36mhash Comparison ")
print(" ")
print("\033[1;31m2] - \033[1;36mhash length")
print(" ")
print("\033[1;31m3] - \033[1;36mhash type ")
print(" ")
print("\033[1;31m4] - \033[1;36mMD5 Encrypt ")
print(" ")
print("\033[1;31m5] - \033[1;36mMD5 Decryption")
print("\033[1;33m=====================================================")
choose =input(">please choose the number: ")
print(" ")
if choose == '1' :
    print("this hash is for Comparison")
    
    hash1= input("> set hash1: ")
    
    hash2= input("> set hash2:  ")
    if hash1 == hash2 :
        
        print("the hash is clean")
    else :
        print("the hash is virus")
if choose == '2' : 
    print("this hash is for lienght")
    
    length = input("> chose your hash:")
    
    print("Length hash is : ", len(length))
if choose == '3':
    print("this hash is for know hash type")
     
    hash = input("> set the hash: ")
    print(" ")
    lenghth = len(hash)
    if lenghth == '32' :
        print("this hash is : [MD5]")   
    if lenghth =='40':
        print("this hash is : [sha1] ")
    if lenghth =='64':
        print("this hash is : [sha256] ")
if choose == '4' :
    print("this hash is for text to MD5")
    word = input("> Enter your text : ")
    md5 = hashlib.md5(word.encode())
    print(md5.hexdigest())

if choose == '5':
    print("this options is for decryption")
    
    hash = input("> enter your hash : ")
    
    file = input("> enter the file name : ")
    
    with open(file , mode='r') as f:
        for line in f:
            line = line.strip()
            if md5(line.encode()).hexdigest() == hash :
                print("[-] password is found : "+ line)
