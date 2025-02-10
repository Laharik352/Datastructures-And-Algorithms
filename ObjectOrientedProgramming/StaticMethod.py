class Calci:
    @staticmethod
    def add(x,y):
        print("The sum:", x+y)
    @staticmethod
    def multiply(x,y):
        print("The product:", x*y)
    @staticmethod
    def average(x,y):
        print("The average:",(x+y)/2)
Calci.add(10,20)
Calci.multiply(10,20)
Calci.average(10,20)
# c=Calci()             Using object reference
# c.average(10,20)