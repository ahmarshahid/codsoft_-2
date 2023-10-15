def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def multiple(x,y):
  return x*y

def divide(x,y):
  return x/y

def main():
  while True:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiple")
    print("4 - Divide")
    choice = int(input("Select the Operator: "))
    if(choice == 1):
      result = add(x,y)
      print(f"The sum of {x} and {y} is {result}")
      break

    elif(choice == 2):
      result = subtract(x,y)
      print(f"The difference of {x} and {y} is {result}")
      break

    elif(choice == 3):
      result = multiple(x,y)
      print(f"The product of {x} and {y} is {result}")
      break;

    elif(choice == 4):
      if(y!= 0):
        result = divide(x,y)
        print(f"The division of {x} and {y} is {result}")
        break

      else:
        print("Division is not possible because y must be not equal to zero for division")
        

if __name__ == "__main__":
  main()