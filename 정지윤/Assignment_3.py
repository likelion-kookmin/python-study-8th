def sum(num_1, num_2) :
    return num_1 + num_2
def m(num_1, num_2) :
    return num_1 - num_2
def mul(num_1, num_2) :
    return num_1 * num_2
def s(num_1, num_2) :
    return num_1 / num_2

num_1 = int(input("first number"))
sign = input("기호")
num_2 = int(input("second number"))

if sign == "+" :
    print(sum(num_1, num_2))
elif sign == "-" :
    print(m(num_1, num_2))
elif sign == "*" :
    print(mul(num_1, num_2))
elif sign == "/" :
    print(s(num_1,num_2))
