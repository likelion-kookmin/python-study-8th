class calculator:
    def sum(self, a, b): # 더하기
        self.a = a
        self.b = b
        print(a+b)
        
    def sub(self, a, b): # 빼기
        self.a = a
        self.b = b
        print(a-b)

    def mul(self, a, b): # 곱하기
        self.a = a
        self.b = b
        print(a*b)

    def div(self, a, b): # 나누기
        self.a = a
        self.b = b
        print(a/b)

cal = calculator()
cal.sum(1,2)
cal.sub(5,3)
cal.mul(4,3)
cal.div(100,10)


class can_div_zero(calculator):
    def div(self, a, b):
        if b==0:
            print("0으로 나눌 수 없다.")
        else:
            print(a/b)

can_div = can_div_zero()
can_div.sum(1,2)
can_div.sub(5,3)
can_div.mul(4,3)
can_div.div(100,10)
can_div.div(10,0)