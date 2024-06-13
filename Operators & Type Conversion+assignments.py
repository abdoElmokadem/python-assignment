# ----------------------------------
# Boolian
# ====================================
# [1] in programming you need to know if your code output is true or false
# [2] Boolian values are the two constant opjects false + true
# ------------------------------------
# name=" "
# print(name.isspace())
# print(100>200)
# print(100>100)
# print(100>90)
# print("="*20)
# # true values
# print(bool("ao"))
# print(bool(100))
# print(bool(100.3))
# print(bool(True))
# print(bool([1,2,3,4]))

# print("="*20)
# # false values
# print(bool(0))
# print(bool(""))
# print(bool(''))
# print(bool(False))
# print(bool(()))
# print(bool({}))
# print(bool(None))

# ======================================
# boolian operator
# ==========================================
# and
# or
# not
# --------------------------------
# agr=17
# Country="moldova"
# rank=91
# print(agr<16)
# print(agr>16)
# print(Country=="egypt")
# print(Country=="moldova")
# print("-"*10)
# print(agr>16 and Country=="moldova" and rank >71)#true
# print(agr>16 and Country=="moldova" and rank >95)#false
# print("-"*20)
# print(agr>16 or Country=="moldova" or rank >71)#true
# print(agr>18 or Country=="egy" or rank >95)#f , if any conditione solved =true
# print("-"*20)
# print(agr>16 )#true
# print(not agr>16)# not true = false
# =================================================================================
# =================================================================================
# assignment Operator
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# ===================================
# +=
# x = 10
# y = 6
# # x += y# like x=x+y
# # x -= y
# # x *= y
# # x /= y
# # x //= y
# # x **= y
# x %= y
# print(x)
# ====================================
# coparison Operator
# ========================
# [ == ] equal
# [ != ] not equal
# [ > ] greater than
#  [ < ] less than
# [ >= ] greater than or equal
#  [ <= ] less than or equal
# =====================================
# print(10 == 10)  # true
# print(10 == 9)  # false
# print("=" * 25)
# print(10 != 10)  # true
# print(10 != 9)  # false
# print("=" * 25)
# print(10 > 10)  # Flase
# print(10 > 9)  # true
# print("=" * 25)
# print(10 < 10)  # false
# print(10 < 9)  # false
# print(10 < 11)  # true
# print("=" * 25)
# print("=" * 25)
# print(10 >= 10)  # true
# print(10 >= 9)  # true
# print("=" * 25)
# print(10 <= 10)  # true
# print(10 <= 9)  # false
# print(10 <= 11)  # true
# print("=" * 25)
# ===========================================================
# التكليف 01

#  وبإستخدام Bool Method     في أول 4 أسطر قم بطباعة 4 أنواع بيانات مختلفة نتيجتهم هي True
#  وبإستخدام Bool Method    قم بطباعة 4 أنواع بيانات مختلفة نتيجتهم هي في السطر الخامس إلى الثامن  False
# print(bool(True))
# print(bool([1, 2]))
# print(bool("os"))
# print(bool(1.2))
# print(bool(""))
# print(bool(()))
# print(bool(False))
# print(bool(0))
# print("#" * 10)
# # ===============2===================
# html = 80
# css = 60
# javascript = 70
# print(bool(html > 50 and css > 50 and javascript > 50))
# print("#" * 10)
# # ===============3===================
# num_one = 10
# num_two = 20
# num = 20
# print(bool(num > num_two or num_one))
# print(bool(num > num_one and num > num_two))
# ==============4=====================
print("#" * 10)
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
result **= 3
print(result)
result %= 26000
print(result)
result //= 5
print(float(result))

print(type(str(result)))
