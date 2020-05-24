# class 과제 : 계산기를 class로 바꾸기 1번 방법

class calculator :
    def __init__(self, num1, num2): # __init__메서드
        self.num1 = num1
        self.num2 = num2

    def sum(self): # sum 메서드를 만들어준다.   #언제는 self만 들어가고, 언제는 객체가 다 들어가고?
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    def double_mul(self):
        return self.num1 ** self.num2
    def remainder(self):
        return self.num1 % self.num2

# cal = calculator()    
# print(cal.sum(10, 2)) # 배운 건 이건데(과제 예시문도)

cal = calculator(10, 2) # num1 = 10, num2 = 2

print(cal.sum())
print(cal.sub())
print(cal.mul())
print(cal.div())   
print(cal.double_mul())    
print(cal.remainder()) # 계산기에선 왜 거꾸로 써야 실행될까

cal2 = calculator(5, 9)
print(cal2.sum())
print(cal2.sub())
print(cal2.mul())

# print(cal.sum(1, 2)) 이 형태로 왜 안되는걸까

# cal2 = calculator()
# print(cal2.sum(1,2))  -> num1이랑 num2를 잃어버렸대 이걸 알려줘야겠다

# cal2 = calculator(self.num1, self.num2)   -> 이건 self가 define되지 않았대
# print(cal2.sum(1,2))

# cal2(self.num1, self.num2)  = calculator()  -> 이건 그냥 함수가 이상하대
# print(cal2.sum(1,2))

cal3 = calculator()
print(cal3.sum(1,2)) 