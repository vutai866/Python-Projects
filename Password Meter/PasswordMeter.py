#Author: Tai Vu
#Program: Password Meter 

#import re library
import re

#Checking for lower case and must has at least 1 lower case character
def lowercase_check(passwrd):
    if re.search("[a-z]" , passwrd):
        return True
    return False    

#Checking for upper case and must has at least 1 upper case character
def uppercase_check(passwrd):
    if re.search("[A-Z]" , passwrd):
        return True
    return False

#Checking for number and must has at least 1 digit
def digit_check(passwrd):
    if re.search("[0-9]", passwrd):
        return True
    return False
 
def input_password():
    passwrd = input("Enter password: ")

    if len(passwrd) >= 8 and uppercase_check(passwrd) and lowercase_check(passwrd) and digit_check(passwrd):
        print("Strong Password")
    else:
        print("Weak Password")    

## Run the program
input_password()