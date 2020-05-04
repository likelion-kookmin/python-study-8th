# class 과제 : 계산기를 class로 바꾸기 2번 방법(과제 예시랑 같은 방법으로 print)

class calculator :
    def sum(self, num1, num2): # sum 메서드를 만들어준다.   # def __init__ 빼고 def sum()에 인수 다 넣어준다.
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1 * num2
    def div(self, num1, num2):
        return num1 / num2
    def double_mul(self, num1, num2):
        return num1 ** num2
    def remainder(self, num1, num2):
        return num1 % num2

cal = calculator() # 객체 생성

print(cal.sum(1, 3))
print(cal.sub(6, 4))
print(cal.mul(9, 3))
print(cal.div(18, 2))   
print(cal.double_mul(99, 4))    
print(cal.remainder(6847, 234))