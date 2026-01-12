import os

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div

}

def choose_operation():
    choosed_operation = input("Choose an operation (+, - , *, /): ")

    while choosed_operation != '+' and choosed_operation != '-' and choosed_operation != '*' and choosed_operation != '/': 
        choosed_operation = input("Choose an operation (+, - , *, /): ")

    return choosed_operation


def calculator ():
    flag = True

    n1 = int(input("Insert the first number: "))

    while flag == True:
        choosed_operation = choose_operation()

        n2 = int(input("Insert the next number: "))

        result = operations[choosed_operation](n1, n2)
        print(f"The result is: {result}")

        decision = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ")

        while decision != 'y' and decision != 'n': 
            decision = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ")

        if decision == 'y':
            n1 = result

        else:
            flag = False
            os.system("cls")
            calculator()

calculator()


