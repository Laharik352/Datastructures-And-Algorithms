class Employee:
    '''Operator Overloading'''
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other): #We have to write this in the Employee class since the first argument is Employee object in e*t
        return self.salary*other.days # self---->e, other------>t
class Timesheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self, other):
        return self.days*other.salary

e = Employee('Durga', 10000)
t = Timesheet('Durga', 25)
print('The total salary is:',e*t)
print('The total salary is:',t*e) # error since timesheet does not have __mul__ method

