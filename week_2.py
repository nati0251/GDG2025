# question 1
x=int(input("number of items you want to buy "))
if x>3:
    print("discount applied")
else:
    print("no discount")

# question 2
def get_expensive_items(prices):
    result = []
    i = 0
    
    while i < len(prices):
        if prices[i] > 100:
            result.append(prices[i])
        i += 1
    
    return result

prices = [120, 45, 300, 85, 150]
result = get_expensive_items(prices)
print(result)

# question 3
def log_user_activity():
    with open("log.txt", "a") as file:
        file.write("User logged in\n")

    with open("log.txt", "r") as file:
        history = file.read()
        print("Full Log History:")
        print(history)

log_user_activity()

# question 4
def get_grades(student_grades):
    x = input("Your name: ")

    try:
        print(f"Your grade is {student_grades[x]}")
        return student_grades[x]
    except KeyError:
        return "Student not found in the system"

grades = {
    "mathew": 55,
    "kudus": 77,
    "ares": 98,
}

print(get_grades(grades))

# question 5
def sales_number(values):
    i = 0
    with open("values.txt", "w") as file:
        while i < len(values):
            file.write(f"{values[i]}\n")
            i += 1

    with open("values.txt", "r") as file:
        content = file.read()
        print(content)


values = [200, 450, 300, 700]
sales_number(values)

# question 6
def calculator():
    sales = []

    try:
        with open("values.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            try:
                number = int(line)     
                sales.append(number)
            except ValueError:
                continue

        total = sum(sales)
        print("Total sales:", total)

    except FileNotFoundError:
        print("values.txt not found.")


calculator()

# question 7
def fizzbuzz(n):
    answer=[]
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 ==0:
            answer.append("fizzbuzz")
        elif i % 3 == 0:
            answer.append("fizz")
        elif i % 5 ==0:
            answer.append("buzz")
        else:
            answer.append(str(i))
    return answer
n=int(input("enter a numbeer "))
print(fizzbuzz(n))

# question 8
def moveZeroes(nums):
    i = 0
    
    for num in nums:
        if num != 0:
            nums[i] = num
            i += 1
            
    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums
x=int(input("how many numbers you want to enter? "))
nums=[]
h=0
while h < x:
    m=int(input(f"enter your {h+1} number "))
    nums.append(m)
    h+=1
print(moveZeroes(nums))

# question 9
def twoSum(nums, target):
    seen = {} 

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i
x=int(input("how many numbers you want to  enter? "))
nums=[]
h=0
while h < x:
    m=int(input(f"enter your {h+1} number "))
    nums.append(m)
    h+=1
target=int(input("enter your target number "))
print(twoSum(nums, target))

# question 10
def Palindrome(x):
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]
x=int(input("enter number"))
print(Palindrome(x))

# question 11
def mySqrt(x):
    
    if x < 2:  
        return x

    left, right = 1, x // 2
    

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
x=int(input(" enter non negative number "))
print(mySqrt(x))

#question 12
def calculator(x):
    value=[]
    i=0
    with open("numbers.txt","a") as file:
        while i < len(x):
            file.write(f"{x[i]}\n")
            i+=1
    with open("numbers.txt","r") as file:
        lines=file.readlines()
    for line in lines:
        line = line.strip()
        
        try:
            number=int(line)
            value.append(number)
        except ValueError:
            continue
    total=sum(value)
    return total
x=[]
h=int(input("number of values : "))
i=0
while i < h:
    j=input(f" enter value {i+1} : ")
    x.append(j)
    i+=1
print(calculator(x))

#question 13
def converter(word):
    upper=[]
    i=0
    with open ("words.txt","w") as file:
        while i < len(word):
            file.write(f"{word[i]}\n")
            i+=1
    with open ("words.txt","r") as file:
        lines=file.readlines()

    for line in lines:
        line=line.strip()

        try:
            if line.isdigit():
                continue
            temp = line.upper()
            upper.append(temp)
        except ValueError:
            continue
    return upper
word=["abs",765,"honey","SDCG"]

print(converter(word))

# question 14
def get_scores(student_grades):
    x = input("Your name: ").lower()

    try:
        return f"your grade is : {student_grades[x]}"
    except KeyError:
        return "Student not found in the system"

score = {
    "john": 85,
    "sara": 92,
    "fraol": 78,
}

print(get_scores(score)) 

#question 15
import re

def word_frequencies(sentence):
    sentence = sentence.lower()                     
    words = re.findall(r"\b\w+\b", sentence)        
    freq = {}                                     
    for w in words:                                 
        freq[w] = freq.get(w, 0) + 1                
    return freq                                     

s = input("Enter a sentence: ")                    
result = word_frequencies(s)                       
print(result)                                      

# question 16
def exchanger(name_key):
    dict = {}

    for name, grade in name_key.items():
        try:
            dict[grade].append(name)
        except KeyError:
            dict[grade] = [name]

    return dict

grades = {"John": "A", "Sara": "B", "Musa": "A"}
print(exchanger(grades))