import re

#Question 1


txt = "(704) 111-1111"

x = re.findall("\(?[0-9]{3}\)?[\- ]?[0-9]{3}[\- ]?[0-9]{4}",txt)

if x:
    print("The number is correct")
else:
    print("Enter in a correct number")
    
    
#Question 2 (matches if there is an @ in the txt, plus a peirod, folowed by com)

txt2 = "a@yahoo.com"

a = re.findall("\S+@+\S+[.]?[c-o]{3}",txt2)
 
if a:
    print("The email is correct")
else:
    print("Enter in a correct email")
    
#Question 3
txt3 = "the 4 books"

b = re.findall("\d",txt3)

if b:
    print("Contains a number")
else:
    print("Doesn't contain a number")
    

#Question 4 (If the user's password is less than 6, it does not accept)

import getpass

def main():
    p = getpass.getpass(prompt='Enter in your password ')
    
    if p > 6:
        print('Password accepted ')
    else:
        print('Enter in a password greater than 6 characters')
        
#Question 5

import re

txt4 = "Tom cried: 'What is going on?'. Then he left the room."

c = re.findall("\S",txt4)

print(c)


#Question 6 (replacing "The" "the" "in" as a stop word)

import re

txt5 = "Here’s to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes. The ones who see things differently — they’re not fond of rules. You can quote them, disagree with them, glorify or vilify them, but the only thing you can’t do is ignore them because they change things. They push the human race forward, and while some may see them as the crazy ones, we see genius, because the ones who are crazy enough to think that they can change the world, are the ones who do."

d = re.sub("the ", " ", txt5)

e = re.sub("in ", " ",d)

f = re.sub("The ", " ",e)

print(f)