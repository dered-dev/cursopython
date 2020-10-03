"""Fibonacci function"""

def fibonacciSequence(count_number) :
    
    # one and two values
    number1 = 0
    number2 = 1
    counter = 0

    # positive number
    if count_number <= 0:
        print("Introduce un número positivo")
    else:
        print("Secuencia de Fibonacci hasta ",count_number,": ")
        while counter < count_number :
            print(number1)
            nextNumber = number1 + number2
            number1 = number2
            number2 = nextNumber
            counter += 1

# get user limit
userNumber = int(input("¿Cuántos numeros necesitas? "))

# invoque function
fibonacciSequence(userNumber)