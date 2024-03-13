#calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2



def calculation():
  number1 = int(input("What is the first number?"))
  should_continue ="y"
  while should_continue == "y":
    number2 = int(input("What is the next number?"))
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide }
    for keys in operations:
      print(keys)

    operator = input("Choose the symbol above")
    result = operations[operator](number1,number2)
    print(f"{number1} {operator} {number2} equals to {result}")
    if (input("Do you want to continue? Choose y, if fresh - choose n")) == "y":
      should_continue ="y"
      number1 = result
    else: 
      should_continue ="n"
      calculation()      
    #else:
    #  print("End")
    #  return

calculation()
