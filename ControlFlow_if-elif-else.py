# name = "abdo"
# country = input("add your country")
# IsStudent = input("are you student, Answer with 'YES' or 'NO'")
# course = "python"
# price = 1000

# if country == "egypt" or country == "KSA":
#     if IsStudent == "YES":
#         print(
#             f"hello {name} because you are from {country} \ncourse price {(price/2)-10} "
#         )
#     else:
#         print(f"hello {name} because you are from {country} \ncourse price {price/2} ")
# elif country == "qater":
#     print(f"hello {name} because you are from {country} \ncourse price {price/3} ")
# elif country == "iraq":
#     print(f"hello {name} because you are from {country} \ncourse price {price/4} ")
# else:
#     print(f"hello {name} course price {price}")

# short hand if
# =========================
# age = int(input("add your age"))
# print("hi you are able to continue") if age > 16 else print("SORRY you can't go")
# ====================
# advaned age details calc
# =====================
# note
# print("*" * 100)
# print(
#     "Hello, You can add your age and choose time unit you want full word or first char "
# )
# print("*" * 100)
# age = int(input("add your age"))
# timeUnit = input("choose time unit u need to know 'months,weeks,days'")
# months = age * 12
# weeks = age * 52
# days = age * 365

# if timeUnit == "months" or timeUnit == "m":
#     print(f"your age equal {months} months".strip())
# elif timeUnit == "weeks" or timeUnit == "w":
#     print(f"your age equal {weeks} weeks".strip())
# elif timeUnit == "days" or timeUnit == "d":
#     print(f"your age equal {days} months".strip())
# =======================================================================
# ========================================================================
# assignment
# ===============
# [1]
"""
num1 = int(input("put first number").strip())
num2 = int(input("put second number").strip())
option = input(" add your emthod you want [=, -, *, /]").strip()
# operate+
if option == "+":
    print(num1 + num2)
# operate[-]
elif option == "-":
    print(num1 - num2)
# operate[*]
elif option == "*":
    print(num1 * num2)
# operate[/]
elif option == "/":
    print(num1 / num2)
"""
# ==========================================================
# [2]
"""
age = int(input("add your age"))
print("App Is Suitable For You") if age > 16 else print("App Is Not Suitable For You")
"""
# ============================================================
# [3]
"""
age2 = int(input("add your age"))
months = age2 * 12
weeks = age2 * 52
days = age2 * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
if age2 < 10 or age2 > 100:
    print("age out of range")
else:
    print(f"Your Age In Months Is {months} months")
    print(f"Your Age In weeks Is {weeks} weeks")
    print(f"Your Age In days Is {days} days")
    print(f"Your Age In hours Is {hours} hours")
    print(f"Your Age In minutes Is {minutes} minutes")
    print(f"Your Age In seconds Is {seconds} seconds")
"""
# ======================================================
# [4]
Countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discout = 30
country = input("Input Your Country").strip().capitalize()
if country in Countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is ${price-discout}"
    )
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
