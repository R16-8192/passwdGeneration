import random
import time #unnecessary

length = int(input("Enter Password length : "))
Alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_{}"
Passwd = random.choices(Alpha, k=length)
print("[ + ] Generating password ...") #unnecessary 
time.sleep(length / 10) #unnecessary 
print(''.join(Passwd)) # ''.join() outputs the result in string
#print(Passwd) This will print a list of chosen choices from Alpha
