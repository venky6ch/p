# Switch Case in Python
def mapper(choice, a, b):
    operation_dict = {1: a + b, 2: a - b, 3: a * b, 4: a / b}
    return operation_dict[choice]


a = int(input("Enter first number :-"))
b = int(input("Enter second number :-"))
operation = 0
while True:
    operation = int(
        input("""Please choice the operation: \n
                        1 : Addition\n 
                        2 : Subtraction\n 
                        3 : Multiplication\n
                        4 : Division\n
                        5 : Exit\n""")
    )
    if operation == 5:
        break
    else:
        print(mapper(operation, a, b))
