import streamlit as st

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def calculator_app():
    st.title("Simple Streamlit Calculator")

    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)

    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.write(f"Result: {result}")

if __name__ == "__main__":
    calculator_app()

# def main():
#  st.title("hello world")
#
# if __name__ == "__main__":
#      main()


