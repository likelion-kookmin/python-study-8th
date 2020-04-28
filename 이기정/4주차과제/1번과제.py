class calculator:

    def __init__(self): self.num = 1
    def sum(self,num1,num2) : print(num1 + num2)
    def sub(self,num1,num2) : print(num1-num2)
    def mul(self,num1,num2) : print(num1*num2)
    def div(self,num1,num2) : 
        self.num = num2
        print(num1/num2)

class can_div_zero(calculator):
    def div(self,num1,num2) : 
        self.num = num2
        if self.num==0 : print("0으로 나눌 수 없습니다.")
        else : print(num1/num2)


cal = calculator()
cal.sum(1,2)
cal.sub(5,3)
cal.mul(4,3)
cal.div(100,10)

can_div = can_div_zero()
can_div.sum(1, 2)     # 출력: 3
can_div.sub(5, 3)     # 출력: 2
can_div.mul(4, 3)     # 출력: 12
can_div.div(100, 10)  # 출력: 10
can_div.div(10, 0)    # 출력: 0으로는 나눌 수 없습니다
