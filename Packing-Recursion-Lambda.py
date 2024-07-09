# ----------------------------------
# Assign1
# ----------------------------------
def get_score(**subject):
    for s, v in subject.items():
        print(f"{s} => {v}")


get_score(math=90, scince=80, languge=70)
print("-" * 40)
get_score(logic=70, problem=50)


# ----------------------------------
# Assign2
# ----------------------------------
def get_people_score(name="unknown", **subject):
    if not subject:
        print(f"hello {name} you have no score to show".title())
    elif name == "unknown":
        for s, v in subject.items():
            print(f"{s} => {v}")
    else:
        print(f"Hello {name} this is your score table".title())
        for s, v in subject.items():
            print(f"{s} => {v}")


get_people_score("osama", math=90, scince=80, languge=70)
print("-" * 40)
get_people_score("mahmoud", logic=70, problem=50)
print("-" * 40)
get_people_score(logic=70, problem=50)
print("-" * 40)
get_people_score("ahmed")
# ----------------------------------
# Assign3
# ----------------------------------
score_list = {"math": 90, "language": 80, "scince": 70}


def get_the_score(name="unknown", **score):
    if not score:
        print(f"hello {name} you have no score to show")
    elif name == "unknown":
        for s, v in score.items():
            print(f"{s} => {v}")
    else:
        print(f"hello {name} this is your score table")
        for s, v in score.items():
            print(f"{s} => {v}")


get_the_score("abdo", **score_list)
print("-" * 40)
get_the_score("abdo")
print("-" * 40)
get_the_score(**score_list)
print("-" * 40)
