name = "abdo"
country = input("add your country")
IsStudent = input("are you student, Answer with 'YES' or 'NO'")
course = "python"
price = 1000

if country == "egypt" or country == "KSA":
    if IsStudent == "YES":
        print(
            f"hello {name} because you are from {country} \ncourse price {(price/2)-10} "
        )
    else:
        print(f"hello {name} because you are from {country} \ncourse price {price/2} ")
elif country == "qater":
    print(f"hello {name} because you are from {country} \ncourse price {price/3} ")
elif country == "iraq":
    print(f"hello {name} because you are from {country} \ncourse price {price/4} ")
else:
    print(f"hello {name} course price {price}")

# short hand if
# =========================
# age = int(input("add your age"))
# print("hi you are able to continue") if age > 16 else print("SORRY you can't go")
# ====================
# advaned age details calc
# =====================
# note
print("*" * 100)
print(
    "Hello, You can add your age and choose time unit you want full word or first char "
)
print("*" * 100)
age = int(input("add your age"))
timeUnit = input("choose time unit u need to know 'months,weeks,days'")
months = age * 12
weeks = age * 52
days = age * 365

if timeUnit == "months" or timeUnit == "m":
    print(f"your age equal {months} months".strip())
elif timeUnit == "weeks" or timeUnit == "w":
    print(f"your age equal {weeks} weeks".strip())
elif timeUnit == "days" or timeUnit == "d":
    print(f"your age equal {days} months".strip())
