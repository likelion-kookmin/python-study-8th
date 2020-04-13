
uinput = input("키를 입력하시오 ")

list = (uinput.split(","))
a = int(list[0])
b = int(list[1])
sum = a + b
min = a - b
gop = a * b
nanu = a / b
namu = a//b
namu2 = a % b 
print("더하기 : i + j = ", sum)
print("빼기 : i - j = ", min )
print("곱하기 : i * j = ", gop)
print("나누기 : i / j = ", nanu)
print("나머지 없이 : i // j = ", namu)
print("나머지만 : i % j = ", namu2)

