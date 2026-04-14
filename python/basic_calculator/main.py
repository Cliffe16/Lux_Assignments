def calculator():
    # Initialize the while loop to iterate over the inputs
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second nummber: "))
        except ValueError:
            print("Error. Enter a valid number.")
            continue

        operation = input("Enter operation (+, -, *, /): ")
    
    # Define the calculator's operations
        try:
            if operation == '+':
                result = num1 + num2 # Store result in a variable to print it in the terminal
            elif operation == '-':
                result = num1 - num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1/num2
            elif operation == '*':
                result = num1 * num2
            else:
                print("Invalid operation")
                continue

            if result is not None:
                print("Result: ", result) # Printable result

    # Account for unexpected errors
        except Exception as e:
            print(f"Error: {e}") 

    # Allow user to terminate the while loop
        choice = input("Do you wish to continue? (y/n): ")
        if choice == 'no' or choice == 'n':
            print("Exiting calculator...")
            break


if __name__ == "__main__":
    calculator()
