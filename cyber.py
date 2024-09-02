import time
import ascii
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','#','@','!','%']

print(f"WELLCOME TO {ascii.art}")

print("WELCOME TO MASSIGE ENCRYPTION AND DECRYPTION")
time.sleep(0.5)

def encrypt(original_text,shift_amount):
    
    c_text=""
    for letter in original_text:
        if letter not in alphabet:
            c_text+= letter
        else:
            position = alphabet.index(letter)+shift_amount
            position %=len(alphabet)
            c_text+=alphabet[position]
    print(f"here is the reslut:{c_text}")
    
def decript(original_text,shift_amount):
    c_text=""
    for letter in original_text:
        if letter not in alphabet:
            c_text += letter
        else:
            position = alphabet.index(letter)-shift_amount
            position %=len(alphabet)
            c_text+=alphabet[position]
    print(f"here is the reslut:{c_text}")
    
def cyber():
    progress = False
    while  not progress :
        direction = input("Enter 'encode'forn encrypt'decode'for decrypi / enter 'exit()' to quit or 'c' to contune:\n").lower()
        if direction=="exit()":
            print("you exit")
            progress=True
        elif direction == "c":
            
            continue
        else: 
            if direction=="encode":
                text = input("Enter youre message\n").lower()
                shift = int(input("enter the number want to shift\n"))
                encrypt(original_text=text,shift_amount=shift)
            
            elif direction=="decode":
                text = input("Enter youre message\n").lower()
                shift = int(input("enter the number want to shift\n"))
                decript(original_text=text,shift_amount=shift)
            
        
            else:
                print("enter valide input")
            
cyber()
        

    
    
    
    