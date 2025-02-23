try:
    num1,num2=map (int, input("enter two numbers separated by a comma: ").split(","))
    result=num1/num2
    print("Result is: ",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid input format, separate numbers by comma!")
except:
    print("Wrong input!")
else:
    print("No exception")
finally:
    print("This is the final part of the code")         