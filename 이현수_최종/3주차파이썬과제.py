def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "NONE"

num1 = input("첫번째 숫자:")
operator =input("operator(+,-,*,/):")
num2 = input("두번째 숫자:")
print("Answer: " + calculator(num1, num2, operator))