import logging

class Calculator:

    def __init__(self,a,b):
        self.a= a
        self.b = b
        self.ans = None

    def add(self):
        print("Addition of: ",self.a, "and ",self.b)
        self.ans = self.a + self.b
        return self.ans

    def mul(self):
        print("Multiplication of:",self.a, "and ",self.b)

        self.ans = self.a*self.b
        return self.ans

    def div(self):
        print("Division of:" ,self.a ,"and " ,self.b)
        self.ans = round(self.a/self.b,2)
        return self.ans

    def sub(self):
        print("Subtraction of:" ,self.a ,"from " ,self.b)
        self.ans = self.a-self.b
        return self.ans


if __name__ == '__main__':

    obj = Calculator(3,4)
    a = obj.add()
    print(a,"\n")
    s = obj.sub()
    print(s,"\n")
    m = obj.mul()
    print(m,"\n")
    d = obj.div()
    print(d,"\n")
    obj = Calculator(5,6)
    a1 = obj.add()
    print(a,"\n")

    logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',level=logging.DEBUG)
    logging.info(a)
    logging.info(s)
    logging.info(m)
    logging.info(d)
    logging.info(a1)
