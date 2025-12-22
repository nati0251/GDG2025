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