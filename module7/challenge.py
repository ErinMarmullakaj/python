#create a function that takes 3 arguments: number1 number2 and the operator
def calculate(n1,n2,operator):
    if operator=="+":
        return n1+n2
    elif operator=="-":
        return n1-n2
    elif operator=="*":
        return n1*n2
    elif operator=="/":
        return n1/n2
    else:
        raise ValueError("invalid operation")

try:
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    operator=input("enter an operation: +,-,*,/")
    rezultati=calculate(num1,num2,operator)

    print(f"the result of {num1} {operator} {num2}:{rezultati}")


except ValueError as e:
    print(f"invalid input {e}")

except ValueError as e:
    print(f"can not divide by 0 {e}")

except Exception as e:
    print(f"error: {e}")

finally:
    print("end of the program")