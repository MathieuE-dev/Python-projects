import random 
import string 

def generator_password(min_Lenght: int = 16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''. join(random.choice(alphabet) for i in range(min_Lenght)) 
    
    return password

password = generator_password()

print (f' Generated Password : {password}')

    
    


    
