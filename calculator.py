# Object Oriented Code of Calculator

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

if __name__ == '__main__':

    print(" ")
    print ("###########################Calculator Started#############################")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(" ")
    obj = Calculator(a, b)
    choice = 1

    while choice != 0:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. Exit")
        print(" ")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Result: ", obj.add())
        elif choice == 2:
            print("Result: ", obj.sub())
        elif choice == 3:
            print("Result: ", obj.mul())
        elif choice == 4:
            print("Result: ", round(obj.div(), 2))
        elif choice == 0:
            print("Calculator Exiting!")
        else:
            print("Invalid choice!!")
