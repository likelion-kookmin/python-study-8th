# 과제1 - 그대로 출력하기

a = input('문장을 입력해 주세요.')
print(a)

# 과제 2 - 계산기 만들기

## print(str("문자열").split(","))
### .split(",") -> ,를 기준으로 입력받은 값 분리 -> 리스트로 만들어주는 거다!

## input, int 활용 기본
# a = int(input("숫자"))
# print(type(a))

# 1
a, b = map(int, input("1. 숫자 입력 (ex 3,4) : ").split(","))

print("더하기 a + b =", a + b)
print("빼기 a - b =", a - b)
print("곱하기 a * b =", a * b)
print("나누기 a / b =", a / b)
print("제곱 a ** b =", a ** b)


# a = input("2. 6숫자 입력 (ex 3,4) : ").split(",") # 3 [3]
# b = input("숫자 입력 (ex 3,4) : ").split(",") # 4 [4]
# print(a, b) -> 리스트가 되니까 +는 되는데 -부터는 안된다.

# print("더하기 a + b =", a + b)
# print("빼기 a - b =", a - b)
# print("곱하기 a * b =", a * b)
# print("나누기 a / b =", a / b)
# print("제곱 a ** b =", a ** b)6

# 2
a, b = input("2. 숫자 입력 (ex 3,4) : ").split(",")
a = int(a)
b = int(b)

print("더하기 a + b =", a + b)
print("빼기 a - b =", a - b)
print("곱하기 a * b =", a * b)
print("나누기 a / b =", a / b)
print("제곱 a ** b =", a ** b)

a = int(input("3. 첫 번째 숫자 입력 : "))
b = int(input("두 번째 숫자 입력 : "))

print("더하기 a + b =", a + b)
print("빼기 a - b =", a - b)
print("곱하기 a * b =", a * b)
print("나누기 a / b =", a / b)
print("제곱 a ** b =", a ** b)