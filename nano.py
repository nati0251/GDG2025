import json
from abc import abstractmethod,ABC
class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass

class Fulltime(Employee):
    def calculate_salary(self):
        return 15000

n=Fulltime.calculate_salary()
print(n)