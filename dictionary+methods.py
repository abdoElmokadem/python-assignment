# dictionary
# ==================
# {1} dict items are inclosed in curly braces
# {2} dict items are contains key : value
# {3} dict key need to be immutable =>(number , string , tuple) list not allowed
# {4} dict value can have any data type
# {5} dict key need to be unique
# {6} dict items are not ordered you access with key
# ==========================================================
# dictionary
# user = {
#     "name": "abdo",
#     "age": 32,
#     "country": "egy",
#     "skills": ["python", "javaScript", "php"],
#     "rating": 1.9,
# }
# print(user)
# print(user["age"])
# print(user.get("country"))
# print(user.keys())
# print(user.values())
# ==============================
# two-dimentional dictionary
# languges = {
#     "one": {"name": "python", "progress": "30%"},
#     "two": {"name": "php", "progress": "1%"},
#     "three": {"name": "JS", "progress": "1%"},
# }
# print(languges["one"])
# print(languges["two"]["name"])
# print(languges["two"]["progress"])

# print(len(languges))
# print(len(languges["one"]))
# # ============================
# # create dictionary from variables
# frame_workOne = {"name": "django", "progress": "20%"}
# frame_workTwo = {"name": "flask", "progress": "10%"}
# frame_workThree = {"name": "pandas", "progress": "60%"}
# all_frame = {"one": frame_workOne, "two": frame_workTwo, "three": frame_workThree}
# print(all_frame["two"])
# print("=" * 50)
# # ==========================
# # dictionary methods
# # clear(),copy(),update()
# frame_workfour = frame_workOne.copy()
# frame_workfour.update({"two": "jquery", "two-progress": "90%"})
# frame_workfour["age"] = "32"
# print(frame_workfour)
# frame_workfour.clear()
# print(frame_workfour)
# -----------------------------------------
# dict methods
# setdefault(),items(),fromkeys(),popitems()
# user = {"name": "abdo"}
# print(user)
# print(user.setdefault("name", "mido"))  # type: ignore #ignore
# print(user)
# print("-" * 20)
# # popitem
# member = {"name": "nono", "age": 23}
# print(member)
# member.update({"skill": "orange"})
# print(member.popitem())
# print("-" * 20)
# # items()
# view = {"name": "nono", "age": 23}
# allitems = view.items()
# print(view)
# view["skill"] = "mandarin"
# print(allitems)
Skills = {
    "skillOne": {"name": "html", "progress": "90%"},
    "skillTwo": {"name": "css", "progress": "80%"},
    "skillThree": {"name": "python", "progress": "30%"},
}
print(f"{Skills['skillOne']['name']} progress Is {Skills['skillOne']['progress']}")
print(f"{Skills['skillTwo']['name']} progress Is {Skills['skillTwo']['progress']}")
print(f"{Skills['skillThree']['name']} progress Is {Skills['skillThree']['progress']}")
# Skills.update({"skillFour": {"name": "AI", "progress": "10%"}})
Skills["skillFour"] = {"name": "AI", "progress": "10%"}
print(f"{Skills['skillFour']['name']} progress Is {Skills['skillFour']['progress']}")
