# Assignment #1-2
val = input("숫자 두개를 입력해주세요 : ")

val = str(val).split(" ")
val = [int (i) for i in val]

print("더하기: i + j = ", val[0] + val[1])
print("빼기: i - j = ", val[0] - val[1])
print("곱하기: i * j = ", val[0] * val[1])
print("나누기: i / j = ", val[0] / val[1])
print("나머지 없이: i // j = ", val[0] // val[1])
print("나머지만: i % j = ", val[0] % val[1])