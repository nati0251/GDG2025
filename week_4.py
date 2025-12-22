# question 1
import json
from abc import abstractmethod,ABC
class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass

class Fulltime(Employee):
    def calculate_salary(self,daily_salary):
        return daily_salary*30

n=Fulltime()
print(n.calculate_salary(1000))

# question 2
import json
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Part_time_employee(Employee):
    def calculate_salary(self,daily_salary,working_day):
        super().calculate_salary()
        return daily_salary * working_day

employee=Part_time_employee()
print(employee.calculate_salary(1000,10))

# question 3
import json
from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on():
        pass
    def turn_off():
        pass

class Washing_machine(Appliance):
    def turn_on(self):
        return "Machine is turned on"
    def turn_off(self):
        return "Machine is turned off"

machine1=Washing_machine()
print(machine1.turn_on())
print(machine1.turn_off())

# question 4
import json
from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def Work(self):
        pass

class Teacher(Person):
    def Work(self):
        return "teacher teaches"

class Doctor(Person):
    def Work(self):
        return "doctor treats patient"

persons=[Teacher(),Doctor()]
for person in persons:
    print(person.Work())
    
# question 5
import json
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        return "woof woof"

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        return "meaw meaw"

animals=[Cat(),Dog()]
for animal in animals:
    print(animal.make_sound())
    
# question 6
import json
from abc import ABC,abstractmethod
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Bus(Transport):
    def move(self):
        super().move()
        return "move on asphalt"

class Train(Transport):
    def move(self):
        super().move()
        return "move on rail way"

transports=[Train(),Bus()]
for transport in transports:
    print(transport.move())

# question 7
import json
data='{"product":"laptop","price":75000,"available":true}'
dictionary=json.loads(data)
print(dictionary)
print(dictionary["product"])
print(dictionary["price"])

# question 8
import json

dictionary={
    "user name": "nati",
    "email": "nati456@gmail.com",
    "acive status": "online"
}

data=json.dumps(dictionary , indent=3)
print(data)

# question 9
import json
from abc import ABC,abstractmethod
files='{"type":"email","type":"sms"}'
class Notification(ABC):
    @abstractmethod
    def file_type(self):
        pass

class Email_Notification(Notification):
    def file_type(self):
        super().file_type()
        data=json.dumps(files)
        return data

class SMS_Notification(Notification):
    def file_type(self):
        super().file_type()
        dictionary=json.loads(files)
        return dictionary

notifications=[Email_Notification(),SMS_Notification()]
for notification in notifications:
    print(notification.file_type())
    
# question 10
import json
from abc import ABC,abstractmethod
json_data='[{"type":"saving"},{"type":"current"}]'
class Account(ABC):
    @abstractmethod
    def get_account_type(self):
        pass

class Saving_account(Account):
    def get_account_type(self):
        return "this is saving account"

class Current_account(Account):
    def get_account_type(self):
        return "this is the current account"

data=json.loads(json_data)
accounts=[]
for item in data:
    if item["type"]=="saving":
        accounts.append(Saving_account())
    elif item["type"]=="current":
        accounts.append(Current_account())

for account in accounts:
    print(account.get_account_type())