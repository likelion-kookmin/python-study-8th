class calculator:
    def sum(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1*num2
    def div(self, num1, num2):
        return num1/num2

class can_div_zero(calculator):
     def div(self, num1, num2):
            if num2==0:
                print("0으로는 나눌 수 없습니다")
            else:
                return num1/num2
    
can_div = can_div_zero()    
print(can_div.sum(1,2))
print(can_div.sub(5,3))
print(can_div.mul(4,3))
print(can_div.div(100,10))
print(can_div.div(10,0))