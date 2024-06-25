def isEven(num):
    if num%2 == 0:
        return "Четное"
    else:
        return "Нечетное"
num = int(input())
print(isEven(num))
