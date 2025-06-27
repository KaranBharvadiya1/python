def printEven(numberList):
    for num in numberList:
        if num % 2 ==0:
            print(f"{num} is Even.")

numberList = []

for i in range(1, 6):
    print(f"Enter number {i}: ", end="")
    number = int(input())
    numberList.append(number)


printEven(numberList)