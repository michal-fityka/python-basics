#calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

num1 = int(input("What is the first number?"))
num2 = int(input("What is the second number?"))


def calculation(number1,number2):
  
  operations = {"+": add, "-": subtract, "*": multiply, "/": divide }
  for keys in operations:
    print(keys)

  operator = input("Choose the symbol above")
  result = operations[operator](number1,number2)
  print(f"{number1} {operator} {number2} equals to {result}")
  should_continue = input("Do you want to continue calculation? If yes - choose y" )
  if should_continue == "y":
    fresh_calculation = input("Do you want to start fresh calculation? If yes - choose y")
    if fresh_calculation == "y":
      num1 = int(input("What is the first number?"))
      num2 = int(input("What is the second number?"))
      calculation(num1,num2)
    next_number = int(input("What is the next number for calculation?" ))
    calculation(result,next_number)
      
  #while should_continue == "y":
  else:
    print("End")
    return


calculation(num1,num2)
