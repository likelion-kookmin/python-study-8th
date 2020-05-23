# Assignment 3-1

class calculator:
    def sum(self, val1, val2):
        print(val1 + val2)

    def sub(self, val1, val2):
        print(val1 - val2)

    def mul(self, val1, val2):
        print(val1 * val2)

    def div(self, val1, val2):
        print(val1 / val2)

    def quo(self, val1, val2):
        print(val1 // val2)

    def remain(self, val1, val2):
        print(val1 % val2)


class can_div_zero(calculator):
    def div(self, val1, val2):
        if val2 == 0:
            print("0으로는 나눌 수 없습니다.")
        else:
            print(val1 / val2)

cal = calculator()
cal.sum(3, 5)
cal.sub(5, 3)  
cal.mul(4, 3)
cal.div(100, 10)

cal.quo(10, 2)
cal.remain(10, 3)

can_div = can_div_zero()
can_div.sum(1, 2)
can_div.sub(5, 3)
can_div.mul(4, 3)   
can_div.div(100, 10)
can_div.div(10, 0)