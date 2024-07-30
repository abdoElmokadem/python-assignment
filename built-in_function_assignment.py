### assign 1
# declare variable
values = (0, 1, 2)
# condition to check if there are any true value
if any(values):
    # if there are true value (my_var = 0)
    my_var = 0
# declare variable contain list
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]
# make a conditionto check at least one true value cause of (or) logic
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    # this part will print Good if condtion true
    print("Good")
else:
    # any thing else will print Bad
    print("Bad")


# output will be => Good

### assign 2
""" here we need to get the value of v 
So lets make a loop with a condition 
- condition will be the sum of list(v)==820
- pow(v,v,v) will alwys = 0
- sum range(40)=sum(1,..,39)will be 780+40=820
"""
v = 40
my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820
# to find v
# v = []
# target_sum = 820
# current_sum = 0

# for i in range(100):
#     v.append(i)
#     current_sum = sum(v)
#     if current_sum == target_sum:
#         break
#     print(v)

# print("Final list:", v)
# print("Final sum:", current_sum)


### assign 3
# n=[]
# targetSum=20
# currentSum=0

# for i in range(20):
#     n.append(i)
#     currentSum=sum(n)
#     if currentSum == targetSum:
#         break
#     print(n)

# print(f"final list : {n}")
# print(f"final sum : {currentSum}")
n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")


### assign 4
def my_all(Allm):
    return all(Allm)


print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []]))
print("#" * 30)


def my_any(Anym):
    return any(Anym)


print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False
print("#" * 30)


def my_min(mine):
    return min(mine)


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

print("#" * 30)


def my_max(maxin):
    return max(maxin)


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
