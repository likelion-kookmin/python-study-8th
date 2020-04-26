class calculator:
    def sum(self,num_1, num_2) :
        return num_1 + num_2
    def m(self,num_1, num_2) :
        return num_1 - num_2
    def mul(self,num_1, num_2) :
        return num_1 * num_2
    def s(self,num_1, num_2) :
        return num_1 / num_2

class can_div_zero(calculator) :
    def s(self,num_1, num_2):
        if num_2 == 0:
            return "0으로는 나눌 수 없습니다."
        else :
            return num_1 / num_2

cal = calculator()
print(cal.sum(1, 2))    # 출력: 3
print(cal.m(5, 3)) # 출력: 2
print(cal.mul(4, 3))   # 출력: 12
print(cal.s(100, 10)) # 출력: 10 여기까지는 필수

can_div = can_div_zero()
print(can_div.sum(1, 2))     # 출력: 3
print(can_div.m(5, 3))     # 출력: 2
print(can_div.mul(4, 3))     # 출력: 12
print(can_div.s(100, 10))  # 출력: 10
print(can_div.s(10, 0))    # 출력: 0으로는 나눌 수 없습니다