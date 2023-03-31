print ("~~~Mini Calulator~~")

def capture_input():
    num1 = float(input("Enter first number here : "))
    num2 = float(input("Enter second number here : "))
    return num1, num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while(True):

    x, y = capture_input()
    result1 = add(x, y)
    result2 = subtract(x, y)
    result3 = multiply(x, y)
    result4 = divide(x, y)

    print ("press 1 for Addition \npress 2 for Subtraction \npress 3 for Multiplication \npress 4 for Division")

    choice = int(input("Enter your choice from 1 - 4: "))


  
    if choice == 1:
        print (f'Result of addition is {result1}')

    elif choice == 2:
        print (f'Result of subtraction is {result2}')

    elif choice == 3:
        print (f'Result of multiplication is {result3}')

    elif choice == 4:
        print (f'Result of division is {result4}')

    else:
        print ("Invalid Input")

    user_choice = int(input("Enter 1 to perform more calculations or any other key to exit"))
    if user_choice != 1:
        break