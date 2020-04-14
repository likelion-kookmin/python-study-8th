# 과제1 - 그대로 출력하기
hi = input('문장을 입력해주세요: ')
print(hi)


# 과제2 - 계산기 만들기
number = input('숫자 두 개를 입력해주세요: ').split(',')
x, y = int(number[0]), int(number[1])
print('더하기: x + y = ', x+y)
print('빼기: x-y = ', x-y)
print('곱하기: x*y = ', x*y)
print('나누기: x/y = ', x/y)
print('몫: x//y = ', x//y)
print('나머지: x%y = ', x%y)