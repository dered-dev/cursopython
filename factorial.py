"""Factorial function"""

def factorial(start) :
    factorial = 1
    # positive number
    if start < 0 :
        print("Introduce un número positivo")
    elif start == 0 :
        print("El factorial de 0 es 1")
    else :
        for i in range(1, start + 1):
            factorial = factorial * i
        
        print("The factorial of",start,"is",factorial)

# get user limit
userNumber = int(input("Introduce un número: "))

# invoque function
factorial(userNumber)