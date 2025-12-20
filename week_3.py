# question 1
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def introduce(self):
        return f"i am {self.name},{self.age} years old"
p1=person("nati",22)
print(p1.introduce())

# question 2
class Dog:
    def __init__(self,sound):
        self.sound=sound
    
    def bark(self):
        return f"{self.sound}"
dog=Dog("woof")
print(dog.bark())

# question 3
class car:
    def __init__(self,make):
        self.make=make
    
    def get_make(self):
        return f"{self.make}"
cars=car("toyota")
print(cars.get_make())

# question 4
class rectangle:
    def __init__(self,width,height):
        self.height=height
        self.width=width
        
    def area(self):
        return self.height * self.width
values=rectangle(4,5)
print(values.area())

# question 5
class student:
    def __init__(self):
        self.__grade=None
    
    def set_grade(self,grade):
        self.__grade=grade
    
    def get_grade(self):
        return self.__grade
values=student()
values.set_grade("A")
print(values.get_grade())

# question 6
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def annual_salary(self):
        return f"{self.name}'s annual salary is {self.salary * 12}"
data=employee("nati",100000)
print(data.annual_salary())

# question 7
class library:
    def __init__(self):
        self.book=None
    
    def add_books(self,book):
        self.book=book
    
    def get_book(self):
        return self.book
data=library()
data.add_books("dertogada")
print(data.get_book())

# question 8
class Animal:
    def make_sound(self):
        print("animal make sound")
        
class Cat(Animal):
    def make_sound(self):
        print("cat says meaw")
animal=Animal()
cat=Cat()
animal.make_sound()
cat.make_sound()

# question 9
class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def info(self):
        return f"brand {self.brand}\n year {self.year}"
        
class Car(Vehicle):
    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model
        
    def info(self):
        return f"brand {self.brand}\n year {self.year}\n model {self.model}\n"
vehicle=Vehicle("toyota",1998)
car=Car("toyota",1998,"hilux")
print(vehicle.info())
print(car.info())

# question 10
class Bank_account:
    def __init__(self,balance=0):
        self.__balance=balance
        
    def Deposit(self,amount):
        self.__balance+=amount
    
    def Withdrawal(self,amount):
        if amount>self.__balance:
            return "insufficient balance"
        self.__balance-=amount
    
    def Get_balance(self):
        return self.__balance
        

account=Bank_account()
account.Deposit(50)
account.Withdrawal(70)
print(account.Get_balance())