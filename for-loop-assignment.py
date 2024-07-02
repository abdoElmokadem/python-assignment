# assign 1
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 1
for n in my_nums:
    if n % 5 == 0:
        print(f"{count}- {n}")
        count += 1
else:
    print("All Numbers Printed")
# ----------------------------------
# assignment 2
for m in range(1, 21):
    if m == 6:
        continue
    elif m == 8:
        continue
    elif m == 12:
        continue
    elif m < 10:
        print(f"0{m}")
    else:
        print(m)
    # print(m)
else:
    print("All Numbers Printed")
# ----------------------------------
#
#  assignment 3
my_ranks = {"Math": "A", "Science": "B", "Drawing": "A", "Sports": "C"}
total_points = 0
for subject, rank in my_ranks.items():
    if rank == "A":
        total_points = 100
    elif rank == "B":
        total_points = 80
    elif rank == "C":
        total_points = 40
    print(f"My Rank in {subject} Is {rank} And This Equal {total_points} Points")
# ----------------------------------
# assignment 4
students = {
    "Ahmed": {"Math": "A", "Science": "D", "Draw": "B", "Sports": "C", "Thinking": "A"},
    "Sayed": {"Math": "B", "Science": "B", "Draw": "B", "Sports": "D", "Thinking": "A"},
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B",
    },
}
total = []
for name in students:
    print("-" * 40)
    print(f"--Student Name is => {name}")
    print("-" * 40)
    for Subject in students[name]:
        items = students[name][Subject]
        if items == "A":
            total_point = 100
            total.append(total_point)
        elif items == "B":
            total_point = 80
            total.append(total_point)
        elif items == "C":
            total_point = 40
            total.append(total_point)
        elif items == "D":
            total_point = 20
            total.append(total_point)
        print(f"{Subject} => {total_point} points")
    print(f"total points for {name} is {sum(total)}")
    total = []
# --------------------------------------------------------
students = {
    "Ahmed": {"Math": "A", "Science": "D", "Draw": "B", "Sports": "C", "Thinking": "A"},
    "Sayed": {"Math": "B", "Science": "B", "Draw": "B", "Sports": "D", "Thinking": "A"},
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B",
    },
}
total = []
for name in students:
    print("-" * 40)
    print(f"--Student Name is => {name}")
    print("-" * 40)
    for material, progress in students[name].items():
        if progress == "A":
            total_point = 100
            total.append(total_point)
        elif progress == "B":
            total_point = 80
            total.append(total_point)
        elif progress == "C":
            total_point = 40
            total.append(total_point)
        elif progress == "D":
            total_point = 20
            total.append(total_point)
        print(f"{material} => {total_point} points")
    print(f"total points for {name} is {sum(total)}")
    total = []
