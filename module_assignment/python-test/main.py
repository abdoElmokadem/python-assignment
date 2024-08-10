# Assign 1
import random

print(f"Random Number Between 10 And 50 => {random.randrange(10,50)}")
print(f"Random even Number Between 2 And 10 => {random.randrange(2,10,2)}")
print(f"Random odd Number Between 1 And 9 => {random.randrange(1,9,2)}")
print(dir(random))
# Assign 2
# import sys

# sys.path.append(r"python-test")
# print(sys.path)
# import my_mod

# my_mod.say_hello("abdo")
# my_mod.say_welcome("abdo")

# Assign 3
# from my_mod import say_welcome
# say_welcome("osos")
# Assign 4
from my_mod import say_welcome as new_welcome

new_welcome("tamer")
