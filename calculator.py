#calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide }

num1 = int(input("What is the first number?"))
num2 = int(input("What is the second number?"))
for keys in operations:
  print(keys)

operator = input("Choose the symbol above")
result = operations[operator](num1,num2)
print(f"{num1} {operator} {num2} equals to {result}")
