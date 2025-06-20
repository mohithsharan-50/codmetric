def addition(numbers):
    return sum(numbers)

def subtraction(numbers):
    result = numbers[0]
    for num in numbers[1:]:
            result -=num
    return result

def multiplication(numbers):
    result = 1
    for num in numbers:
        result *=num
    return result

def division(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /=num
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def get_multiple_num():
    while True:
        try:
            nums = input("enter num for calculation with spaces: ").split()
            numbers = [float(num) for num in nums]
            return numbers
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

"""def get_two_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
"""
while True:
    print("\nSimple Calculator")
    print("Select operation:")
    print("1. Addition (multiple numbers)")
    print("2. Subtraction (multiple numbers)")
    print("3. Multiplication (multiple numbers)")
    print("4. Division (multiple numbers)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice == '1':
        numbers = get_multiple_num()
        result = addition(numbers)
        print(f"The result of addition is {result}")
    elif choice == '2':
        numbers = get_multiple_num()
        result = subtraction(numbers)
        print(f"The result of subtraction is {result}")
    elif choice == '3':
        numbers = get_multiple_num()
        result = multiplication(numbers)
        print(f"The result of multiplication is {result}")
    elif choice == '4':
        numbers = get_multiple_num()
        result = division(numbers)
        print(f"The result of division is {result}")
    else:
        print("Invalid choice. Please select a valid option (1-5).")