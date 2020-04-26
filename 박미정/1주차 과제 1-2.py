one, two = input("숫자 두 개를 입력해주세요").split(",")

one = int(one)
two = int(two)

print("더하기: i + j =" , one + two)
print("빼기 : i - j = " , one - two)
print("곱하기 : i * j =", one * two)
print("나누기 : i / j =", one / two)
print("나머지없이 : i // j = ", one//two)
print("나머지만 : i % j=", one % two)