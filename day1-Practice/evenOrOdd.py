def evenOrOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"
    
number = int(input("Enter a number: "))

print(f"The number {number} is {evenOrOdd(number)}.")