# ==========================
# User input
# # -----------------------------
# Fname, Mname, Lname = [
#     input("put your first name"),
#     input("put your middel name"),
#     input("put your last name"),
# ]
# Fname = Fname.capitalize().strip()
# Mname = Mname.capitalize().strip()
# Lname = Lname.capitalize().strip()
# print(f"hello {Fname:1s} {Mname:1s} {Lname} happy to see you")
# # ==============================
# # practical slicing email

# TheName = input("what's your name")
# TheEmail = input("what's your email")
# Username = TheEmail[: TheEmail.index("@")]
# Company = TheEmail[TheEmail.index("@") + 1 :]
# print(f"hello {TheName} your email is {TheEmail}")
# print(f"yous username is {Username} \nyour company is {Company}")
# # ====================================
# full age details
# ===========================
# input person age
# need to add age calculate !!!
age = int(input("thanks to add your age "))
if age > 65:
    print("search for cemetry")
else:
    age_Months = age * 12
    age_Weeks = age_Months * (30 / 7)
    # age_weeks = age_Mont 33hs * 4
    age_Days = age_Weeks * 365
    age_Hours = age_Days * 24
    age_Minutes = age_Hours * 60
    age_Seconds = age_Minutes * 60

    print(f"your age by months {age_Months}")
    print(f"your age by weeks {age_Weeks:.2f}")
    print(f"your age by days {age_Days:,.2f}")
    print(f"your age by hours {age_Hours:,.2f}")
    print(f"your age by minutes {age_Minutes:,.2f}")
    print(f"your age by seconds {age_Seconds:,.2f} ")
