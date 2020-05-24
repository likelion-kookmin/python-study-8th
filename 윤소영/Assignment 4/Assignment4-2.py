# class 과제 2 : 상속받은 calss 만들기(과제 1, 1번방법에서 이어함)

class calculator :
    def __init__(self, num1, num2): # __init__메서드
        self.num1 = num1
        self.num2 = num2

    def sum(self): # sum 메서드를 만들어준다.
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

cal = calculator(10, 2) # num1 = 10, num2 = 2

print(cal.sum())
print(cal.sub())
print(cal.mul())
print(cal.div())   
print(cal.double_mul())    
print(cal.remainder())

# 여기까지는 과제1과 동일

class can_div_zero(calculator): # 상속했다

    def div(self): 
        if self.num2 == 0:  
            return "0으로는 나눌 수 없습니다"
        else:      
            return self.num1 / self.num2
    
    def remainder(self):
        if self.num2 == 0:  
            return "0으로는 나눌 수 없습니다"
        else:      
            return self.num1 / self.num2

can_div = can_div_zero(5, 0)  # num1 = 5, num2 = 0

print(can_div.sum())
print(can_div.sub())
print(can_div.div())
print(can_div.double_mul())
print(can_div.remainder())  # 얘도 나누기 결과값이라 if 해줘야 함!
        


