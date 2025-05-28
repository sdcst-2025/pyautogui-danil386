#!working with time

import random
import keyboard
import time

"""
Task 1
Basic Assignment:
Create a program to display 10 characters on screen, one at a time,
to the user.  They have to press that key to advance to the next character.
Tell the user how long it took them to press all 10 characters.

Alternately, you can select a random word from a list of words that you provide.
Have the user type in the word before the next word is selected.  This version
is easier because you can use the existing input() command that you are more
familiar with.

Your assignment should make appropriate use of functions to break the
code up into more manageable sections.  

Your assignment will be graded on the following criteria:

functionality (does it work the way it is intended)
modularity (is it broken up into functions to make your main block momre readable)
appropriate use of return values and input parameters

"""

# The code shown below is one way to read a single 
# keystroke from the keyboard and store it into 
# a variable. We will use it as the basis for this 
# assignment.

starttime = time.time()
print("Type the character that shows up on screen.")
letters = ["q","w","e","r","t","y","u","i","o","p"]
x=0

for x in range (0,10):
    f = False
    currentletter = letters[x]
    print(currentletter)
    while f == False:
        z = keyboard.read_key()
        if z == currentletter:
            break
currenttime = time.time()
elapsed = currenttime - starttime
print(f"Your elapsed time is {elapsed}")
