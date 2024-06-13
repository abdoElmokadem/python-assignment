# # this is the first assignment
# # next the second assign
# # varibles type string
# name = "abdelrahman"
# age="31"
# country="egypt"
# # third assign
# print("name:"+name)
# print("age:"+age)
# print("country:"+country)
# # fourth assign
# print("hello, my name is"+" "+name+" "+"and iam"+" "+age+" "+"years old and i live in"+" "+(country))
# # FIFTH ASSIGN
# print(type(name))
# print(type(age))
# print(type(country))

# # -----------------
# a = "ali"
# o = "omar"
# print(o + " " + a)
# print(10+30)
# print(60-30)
# print(60/3)
# print(60*3)
# print(5-10*100)
# print((5-10)*100)
# # modulus باقي القسمه
# print(8 % 2)#0
# print(9 % 2) #1
# print( 31 % 4)
# #  exponent الاوس
# print(2**5)
# print(5**4)
# # floor divison
# print(100 // 20)#5
# print(120 // 20)#6
# print(130 // 20)#6
# print(140 // 20)#7
# print(160 // 20)#8
# print(162 // 20)#8
# -------------------------#
# lists
# [1] list items are enclosed in square brackets
# [2]list are orderd, use index to access items
# [3]list are mutable => add, delete, edit
# [4]list items are not unique
# [5]list can have different data types
# --------------------------#

# MyListA = ["one", "two", "three", 1, 1000,True]
# print(type(MyListA))
# print(MyListA[0])
# print(MyListA[-1])
# print(MyListA[3])# or [-3]
# print(MyListA[-3])
# print(MyListA[1:4])
# print(MyListA[:4])
# print(MyListA[1:])
# print(MyListA[::2])
# MyListA[-1]=False
# print(MyListA[-1])
# print(MyListA)

# MyListA[-3]= 4
# print(MyListA[-3])
# MyListA[0:3]= [1,2,3]
# print(MyListA)

# # --------------------------
# # list methods
# # --------------------------
# #append()
# extend()
# sort()
# reverese()
# ----------------------------
# MyNew_list = ["mido", "mano", "dodo", "bebo"]
# MyListA.append(2)
# MyListA.append("four")
# MyListA.append(MyNew_list)
# print(MyListA)
# print(MyListA[8])#list MyNew_list
# print(MyListA[8][3])#bebo
# MyListA.extend(MyNew_list)
# print(MyListA)
# MyListA[8]=8
# print(MyListA)
# MyListA.reverse()
# print(MyListA)
################################################################################
# list methods
# ----------------------
# clear()
# a = [1, 2, 3, 4]
# a.clear()
# print(a)
# # copy
# b = [2, 4, 6, 8]
# c = b.copy()
# print(c)
# # count()
# d = [1, 2, 3, 4, 2, 5, 2, 5, 7, 6]
# print(d.count(2))
# print(d.count(5))
# # remove()
# e = [1, 2, 3, 4, 6, 4]
# e.remove(1)
# print(e)
# # index()
# f = ["ahmed", "ali", "said", "khalid"]
# print(f.index("said"))
# print(f.index("khalid"))
# # insert()
# g = ["ahmed", "ali", "said", "khalid"]
# g.insert(3, "bebo")
# print(g)
# # pop()
# print(g.pop(3))
# g.append(5)
# print(g)
# g[4] = 7
# print(g)

# #####################################
# ---------------------1---------------
# Freinds = ["mano", "dodo", "bebo", "boda", "mido", "moaaz"]
# print(Freinds[0])
# print(Freinds[-6])
# # print(Freinds.pop(0))
# print(Freinds[-1])
# print(Freinds[5])
# # print(Freinds.pop(-1))
# # ---------------------2---------------
# # Freinds = ["mano", "dodo", "bebo", "boda", "mido", "moaaz"]
# print(Freinds[::2])
# print(Freinds[1::2])
# # -------------------------------3-----------------
# print(Freinds[1:4])
# print(Freinds[-2:])
# # -------------4-----------------------------------
# Freinds[-2:] = ["Elzero", "Elzero"]
# print(Freinds)
# # ---------5-----------------------------------
# Freinds.insert(0, "naser")
# Freinds.append("nassar")
# print(Freinds)
# ----------------------6-----------------
# Friends = ["mano", "dodo", "bebo", "boda", "mido", "moaaz"]

# Friends.remove("mano")
# Friends.remove("dodo")
# print(Friends)
# Friends.remove("moaaz")
# print(Friends)
# -------------7-----------------------------------
# Friends = ["mano", "dodo"]
# School = ["bebo", "boda"]
# Work = ["mido", "moaaz"]
# Friends.extend(School)
# Friends.extend(Work)
# print(Friends)
# =========================8======================
# Friends = ["mano", "dodo", "bebo", "boda", "mido", "moaaz"]
# Friends.sort(reverse=False)
# print(Friends)
# Friends.sort(reverse=True)
# print(Friends)
# ---------------------9-----------------------
# Friends = ["mano", "dodo", "bebo", "boda", "mido", "moaaz"]
# print(Friends.__len__())
# ========================10====================
# Lang = ["c#", "c++", "js", "python", "php"]
# Fram_Work = ["django", "jquary", "flask"]
# Lang.append(Fram_Work)
# print(Lang)
# Lang[-1].append("React")
# print(Lang)
# ###################################################################
