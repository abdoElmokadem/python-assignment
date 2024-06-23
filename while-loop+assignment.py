# while loop assignments

# assignment 1
num = int(input("add a number > 0"))
numList = []
if num > 0:
    while num > 1:
        num -= 1
        if num == 6:
            continue
        elif num == 0:
            break
        print(num)
        numList.append(num)
    print(f"{len(numList)} Numbers Printed Successfully.")
else:
    print("Number 0 Is Not Larger Than 0")

# assignment 2
friends = ["Mohamed", "Shady", "Ahmed", "eman", "sherif"]
ignored = []
index = 0
while len(friends) > index:
    if friends[index][0].isupper():
        print(friends[index])
    elif friends[index].islower():
        ignored.append(friends[index])
    index += 1
print(f"{len(ignored)} ignored friends name counted")

# assignment 3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))

# assignment 4

my_frinds = []
# max frinds to add [4]
maxFriends = 4
# make loop
while maxFriends > 0:
    # make name input [string]
    Fname = input("add friend name with lower case".strip())
    # if name writen with upper case
    if Fname.isupper():
        print("Invalid Name")

    # if name wrien with lower case
    elif Fname.islower():
        my_frinds.append(Fname.capitalize().strip())
        maxFriends -= 1
        print(f"friend {Fname.strip()} has added and transformed to Capitalize.")
        print(f"{maxFriends} names has left")

    # if name writen with capitalize
    elif Fname.capitalize():
        my_frinds.append(Fname.strip())
        maxFriends -= 1
        print(f"friend {Fname.strip()} has added ")
        print(f"{maxFriends} names has left")
else:
    print("freinds list is full")
