# ===================
# SET
# ===================
# {1} set items are enclosed in curly braces
# {2} set items not ordered and not indexed
# {3} set indexing and slicing can't be done
# {4} set has only immutable data types (numbers , string , tuple) list and dic are not enclude
# {5} set items is unique
# ==========================
# not ordered and not indexed
# My_set1 = {"one", "two", 3}
# print(My_set1)  # every time run code result will change
# # -----------------------
# # slicing can't done
# Set_One = {1, 2, 3, 4, 5, 6}
# # print(Set_One[0:3]) #error will show cause slicing can't done
# # ==================================
# # set has only immutable data types (numbers , string , tuple)
# # set_2 = {True, 10.5, "abdo", 11, [1, 2, 3]}
# # print(set_2)#TypeError: unhashable type: 'list'
# set_3 = {True, 10.5, "abdo", 11, (1, 2, 3)}
# print(set_3)
# # ======================================
# # set items is unique
# # ==================================
# set_4 = {1, 1, 2, "abdo", "maged", "abdo"}
# print(set_4)  # only unique item will show{1,2,"abdo","maged"}
# -------------------------------
# set methods
# --------------------------------
# # differance()
# a = {1, 2, 3, 4}
# b = {1, 3, "m", "h"}
# print(b)
# print(a)
# print(b.difference(a))  # another method to do same (a-b)
# print(a.difference(b))

# print("-" * 30)  # separator

# # -----------------------------
# # difference_update()
# c = {1, 2, 3, 4}
# d = {1, 3, "m", "h"}
# print(c)
# c.difference_update(d)
# print(c)

# print("=" * 40)  # separator
# # --------------------------------
# # intersection()
# e = {1, 2, 3, 4, "m", "r"}
# f = {1, 3, "m", "h"}
# print(e)
# print(e.intersection(f))  # e&f
# print(e)

# print("=" * 40)  # separator
# # intersection_update
# g = {1, 2, 3, 4, "m", "r"}
# h = {1, 3, "m", "h"}
# print(g)
# g.intersection_update(h)
# print(g)

# print("=" * 40)  # separator
# # issuperset(),issubset(), isdisjoint()
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {1, 2, 3, 4, 5}
# e = {10, 11, 12, 15}
# f = {10, 11, 12}
# print(a.issuperset(b))  # true

# print("=" * 5)  # separator

# print(b.issuperset(c))
# print("=" * 10)  # separator
# print(b.issubset(a))
# print("=" * 20)  # separator
# print(c.isdisjoint(e))
# print("=" * 30)  # separator
# print(e.isdisjoint(f))
# print("=" * 40)  # separator
# j = e.union(f)
# print(j)
# ========================================
# assignments
# ------------------------1-------------------
# my_list = [1, 2, 3, 3, 4, 5, 1]
# unique_list = list(set(my_list))
# print(unique_list)
# print(type(unique_list))
# print(unique_list[0:4])
# =============================2==================
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}
# print(nums.union(letters))
# print(nums | letters)
# nums.update(letters) # type: ignore
# merged = nums
# print(merged)
# =====================3==============================
# set_1 = {1, 2, 3}
# set_2 = {"a", "b"}
# print(set_1)
# set_1.clear()
# print(set_1)
# # set_1.add("a")
# # set_1.add("b")
# set_1.update(set_2)
# print(set_1)
# set_1.discard("c")
# print(set_1)
# ==========================4====================
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}
# print(set_one.issubset(set_two))
# # print(set_two.issuperset(set_one))
