class calculator:
    def sum(self, n1, n2):
        print(n1 + n2)
    
    def sub(self, n1, n2):
        print(n1 - n2)
    
    def mul(self, n1, n2):
        print(n1 * n2)
    
    def div(self, n1, n2):
        print(n1 / n2)

    def quo(self, n1, n2):
        print(n1 // n2)

    def remain(self, n1, n2):
        print(n1 % n2)
    
class can_div_zero(calculator):
    def div(self, n1, n2):
        if n2 == 0:
            print("0으로는 나눌 수 없습니다")
        else:
            print(n1 / n2)

    # 요건 보너스~!
    def quo(self, n1, n2):
        if n2 == 0:
            print("0으로는 나눌 수 없습니다")
        else:
            print(n1 / n2)
    

if __name__ == "__main__":
    # test1
    cal = calculator()
    cal.sum(1, 2)    # 출력: 3
    cal.sub(5, 3)    # 출력: 2
    cal.mul(4, 3)    # 출력: 12
    cal.div(100, 10) # 출력: 10 여기까지는 필수
    cal.quo(10, 2)   # 출력: 5 여기부터는 선택사항
    cal.remain(10, 3)# 출력: 1 

    print('='*30)

    can_div = can_div_zero()
    can_div.sum(1, 2)     # 출력: 3
    can_div.sub(5, 3)     # 출력: 2
    can_div.mul(4, 3)     # 출력: 12
    can_div.div(100, 10)  # 출력: 10
    can_div.div(10, 0)    # 출력: 0으로는 나눌 수 없습니다