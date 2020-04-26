# Program make a simple calculator


# This function takes two numbers
def numbers ():
    No1 = float(input("Enter first number: "))
    No2 = float(input("Enter second number: "))
    return No1, No2

# This fucntion takes input from user
def take_choice():
    val = input("Enter choice(0/1/2/3/4): ")
    return val;

# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print(" ")
print("0.Exit")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print(" ")

# Take input from the user

choice = take_choice()
print(" ")

while (choice != '0'):

    if choice == '1':
        num1, num2 = numbers()
        print("Ans = ", add(num1,num2))
        print(" ")
        choice = take_choice ()

    elif choice == '2':
        num1, num2 = numbers()
        print("Ans = ", subtract(num1,num2))
        print(" ")
        choice = take_choice ()

    elif choice == '3':
        num1, num2 = numbers()
        print("Ans = ", multiply(num1,num2))
        print(" ")
        choice = take_choice ()

    elif choice == '4':
        num1, num2 = numbers()
        print("Ans = ", divide(num1,num2))
        print(" ")
        choice = take_choice ()

    else:
        print("Invalid input! Enter the correct choice")
        print(" ")
        choice = take_choice ()

if choice == '0':
    print ("Calculator Exit")
