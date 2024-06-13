# --------------------------------------
# Tuple
# --------------------------------------
# (1) Tuple items Are in parentheses()
# (2) you can remove parentheses() if you want
# (3) Tuple are ordered, to use index to access items
# (4) tuple are immutable => you can't add or delete
# (5) Tuple items are not unique
# (6)Tuple can have different data types
# (7) Oprerators used in string and lists avilable in tuple
# ======================================
# tuple syntax & type test

# T_uple1 = ("osama", "mido")
# T_uple2 = "osama", "mido"
# print(T_uple1)
# print(T_uple2)
# print(type(T_uple1))
# print(type(T_uple2))
# ----------------------------
# Tuple indexing

# T_uple3 = (1, 2, 3, 4, 5, 6)
# print(T_uple3[0])  # [1]
# print(T_uple3[3])  # [4]
# print(T_uple3[-3])  # [4]
# print(T_uple3[-1])  # [6]
# -------------------------
# # Tuple assign values
# T_uple4 = (1, 2, 3, 4, 5, 6)
# T_uple4[1] = "two"
# # print(T_uple4)  #tuple' object does not support item assignment
# ----------------------------------
# #  tuple items
# T_uple5 = (1, 2, 3, 4, 5, 4, "zero", "hero", True)
# print(T_uple5[0])
# print(T_uple5[6])
# print(T_uple5[-1])
# -----------------------------------
# Tuple with one element
# T_uple6 = ("osos",)
# # copmilar will see tuple as a string if it contains one item so to make it see as tuple we put comma(,)after the item
# T_uple7 = "osos"
# print(T_uple6, T_uple7)
# print(type(T_uple6))
# print(type(T_uple7))

# print(len(T_uple6))
# # --------------------------
# # tuple concatenation
# a = (1, 2, 3, 4)
# b = ("c", "d", "e", "f")
# c = a + b
# print(c)
# # =========================
# # tuple,list,string,repeat (*)
# mString = "dodo"
# mList = [1, 2, 3, 4]
# mTuple = ("one", "two", "three")
# print(mString * 2)
# print(mList * 2)
# print(mTuple * 2)
# # ================================
# # Tuple methods
# # count() ,index()
# d = (1, 2, 3, 4, 5, 55.6)
# print(d.count(5))
# e = (1, "re", 4, "nd", 5)
# print("the position of index is : {:}".format(e.index("re")))
# print(f"the position of index is : {e.index('re')}")
# # ===================================
# tuple distruct
# f = (1, 2, 3)
# # a, b, c = 1, 2, 3
# a, b, c = f  # same as above
# print(a)
# print(b)
# print(c)
# g = ("a", "v", 2, "w")
# a, b, _, c = g  # to ignore item put (_)
# print(a)
# print(b)
# print(c)
# ----------------------------------------
# assignments
# -----------------------1--------------------
My_name = ("abdelrahman",)
print(My_name)
print(type(My_name))
# ==========================2====================
friends = ("Osama", "Ahmed", "Sayed")
friends = ("Elzero", "Ahmed", "Sayed")
print(friends)
print(type(friends))
print(f"{len(friends)} element")
# ==============================3==================
nums = (1, 2, 3)
letters = ("A", "B", "C")
T_mix = nums + letters
print(f"nums_and_letters_in one = {T_mix}")
print(f"{len(T_mix)} element")
# =================================4===================
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)
