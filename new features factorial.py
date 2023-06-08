user = int(input('enter range:'))
result = 1

for number in range(1, user+1):
    result *= number
    print("Factorial of", number, "is", result)
    print('* '*number)
    

