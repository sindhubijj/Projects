#Password Generator 
import random 
import string 

#Function for generating a random password with the general requirements
    #Requirements: letters, numbers, and punctuation
def pswd_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    pswd = ''.join(random.choices(characters, k = length))
        #random.choice is a method which randomly chooses elements based on specified parameters
    return pswd

#User can specify the length of the password 
length = int(input("Enter password length: "))

pswd = pswd_generator(length) #generate password    
print("Your password is: ", pswd) #print password