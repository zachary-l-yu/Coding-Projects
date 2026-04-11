# a program that generates a unique password (CLI)
# started: April 10, 2026
# finished: April 10, 2026
import random
import time


password = ""
random_characters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9',
    '!','@','#','$','%','^','&','*','(',')','-','_','=','+',
    '[',']','{','}',';',':',',','.','<','>','/','?'
]
# infinite loop to check errors
while True:
    length = int(input("Length (must be at least 8): "))

    if length >= 8:
        break
    else:
        print("Length must be more than or equal to 8!")
        time.sleep(3)


# until the password is as long as the user wants,
# add a random character to the password
while len(password) != length:
    password += random.choice(random_characters)
    
time.sleep(2)
print("Generating password...")

time.sleep(3)
print("Password created!")

time.sleep(2)
print(password)
