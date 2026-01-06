try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Select Operation to perform:\n 1. Press + for addition\n 2. Press - for subtraction\n 3. Press * for multiplication\n 4. Press / for division")

    operation = input("enter operation:")

    match operation:
        case "+":
            print(f"The result is : {a+b}")     
        case "-":
            print(f"The result is : {a-b}")     
        case "*":
            print(f"The result is : {a*b}")     
        case "/":
            print(f"The result is : {a/b}")     
        case default:
            print(f"There is an invalid operation")     
     
except Exception as e:
    print(f"An error occurred: {e}")    