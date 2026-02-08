try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)

except ValueError:
    print("Non-number input")

except ZeroDivisionError:
    print("Division by zero is not allowed")
    
finally:
    print("Program is finished")
