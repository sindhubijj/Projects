#Calculator App

#define all the functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#While loop to display Calculator Menu Options 
while True: 
    print("Operation")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    #User inputs an operation choice and inputs two numbers 
    choice = input("Enter an operation choice (1, 2, 3, or 4): ")

    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter the first value: "))
        y = float(input("Enter the second value: "))
    
    #Perform the corresponding calculcation based on user input
    if choice == '1':
        print(x, "+", y, "=", add(x, y))
    elif choice == '2':
        print(x, "-", y, "=", subtract(x,y))
    elif choice == '3':
        print(x, "*", y, "=", multiply(x,y))
    elif choice == '4':
        print(x, "/", y, "=", divide(x, y))
    
    break

else:
    print("Uh Oh! Input is Invalid.")

