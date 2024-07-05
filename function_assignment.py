### assignment 1
def calculate(n1, n2, m="add"):
    m = m.lower()
    if m == "subtract" or m == "s":
        print(n1 - n2)
    elif m == "multibly" or m == "m":
        print(n1 * n2)
    elif m == "add" or m == "a":
        print(n1 + n2)
    else:
        print("wrong method".capitalize())


calculate(22, 2, "")


### assignment 2
def addetion(*nu):
    total = 0
    for i in nu:
        if i == 10:
            continue
        elif i == 5:
            total -= 5
        else:
            total += i
    return total


addetion(10, 20, 30, 10, 15)
addetion(10, 20, 30, 10, 15, 5, 100)


### assignment 3
def show_skills(name, *skill):
    if not skill:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Is ")
        for skil in skill:
            print(f"- {skil}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")


### assignment 4
def hello(name="Unknown", age="Unknown", contry="Unknown"):
    return f"hello {name} your age is {age} and your contry is {contry}"


hello("Osama", 38, "Egypt")
hello()
