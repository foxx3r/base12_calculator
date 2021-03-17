from BaseConverter import duo

while True:
    print("=" * 20)
    operation = int(input("1 - addition\n2 - subtraction\n3 - multiplication\n4 - division\n-> "))
    print("=" * 20)
    if operation == 1:
        a = duo(input("type your first number: ")).decimal()
        b = duo(input("type your second number: ")).decimal()
        print("=" * 20)
        print(f"The result is {duo(a + b).string}")
    elif operation == 2:
        a = duo(input("type your first number: ")).decimal()
        b = duo(input("type your second number: ")).decimal()
        print("=" * 20)
        print(f"The result is {duo(a - b).string}")
    elif operation == 3:
        a = duo(input("type your first number: ")).decimal()
        b = duo(input("type your second number: ")).decimal()
        print("=" * 20)
        print(f"The result is {duo(a * b).string}")
    elif operation == 4:
        a = duo(input("type your first number: ")).decimal()
        b = duo(input("type your second number: ")).decimal()
        print("=" * 20)
        print(f"The result is {duo(a / b).string}")
    else:
        print("There is no such operation for that")
