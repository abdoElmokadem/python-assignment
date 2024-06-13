print("choose method you want")
var1 = input("put the method (sum , min ,divid ,multible)")
num1 = input("enter first num")
num2 = input("enter second num")
Result1 = float(num1) + float(num2)
Result2 = float(num1) - float(num2)
Result3 = float(num1) / float(num2)
Result4 = float(num1) * float(num2)
if var1 == "sum":
    print(Result1)
elif var1 == "min":
    print(Result2)
elif var1 == "divid":
    print(Result3)
elif var1 == "multible":
    print(Result4)
