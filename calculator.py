def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Cannot divide by zero."
    return first_number / second_number


def power(base_number, exponent):
    return base_number ** exponent


def squared_root(number):
    if number < 0:
        return "Square root is not defined for negative numbers."
    return number ** 0.5


def factorial(number):
    try:
        numeric_value = float(number)
    except (TypeError, ValueError):
        return "Factorial is only defined for whole numbers."

    if not numeric_value.is_integer():
        return "Factorial is only defined for whole numbers."

    integer_value = int(numeric_value)
    if integer_value < 0:
        return "Factorial is not defined for negative numbers."
    if integer_value == 0:
        return 1

    result = 1
    for value in range(1, integer_value + 1):
        result *= value
    return result


def main():
    while True:
        print("Available operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Quit")

        choice = input("Choose an operation: ").strip().lower()

        if choice in ("8", "quit"):
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid option. Please choose a valid operation.")
            continue

        try:
            if choice in {"5", "6", "7"}:
                if choice == "5":
                    base_number = float(input("Enter the base number: "))
                    exponent = float(input("Enter the exponent: "))
                    result = power(base_number, exponent)
                    print(f"Power result: {result}")
                elif choice == "6":
                    number = float(input("Enter a number: "))
                    result = squared_root(number)
                    if result == "Square root is not defined for negative numbers.":
                        print(result)
                    else:
                        print(f"Square root result: {result}")
                else:
                    number = float(input("Enter a number for factorial: "))
                    if number % 1 != 0:
                        print("Factorial is only defined for whole numbers.")
                        continue
                    result = factorial(int(number))
                    if result == "Factorial is not defined for negative numbers.":
                        print(result)
                    else:
                        print(f"Factorial result: {result}")
            else:
                first_number = float(input("Enter the first number: "))
                second_number = float(input("Enter the second number: "))

                if choice == "1":
                    result = add(first_number, second_number)
                    print(f"Addition result: {result}")
                elif choice == "2":
                    result = subtract(first_number, second_number)
                    print(f"Subtraction result: {result}")
                elif choice == "3":
                    result = multiply(first_number, second_number)
                    print(f"Multiplication result: {result}")
                else:
                    result = divide(first_number, second_number)
                    if result == "Cannot divide by zero.":
                        print(result)
                    else:
                        print(f"Division result: {result}")
                print()
        except ValueError:
            print("Please enter valid numbers.")
            continue


if __name__ == "__main__":
    main()