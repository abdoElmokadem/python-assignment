# convert text to csv
# =============================
import pandas

# print(dir(pandas))
# My_Data = pandas.read_csv("example.txt")
# My_Data.to_csv("example.csv", index=None)
My_Data = pandas.read_csv("example.txt")
# My_Data.columns = ["name", "phone"]
My_Data.to_csv("example.csv", index=False)
