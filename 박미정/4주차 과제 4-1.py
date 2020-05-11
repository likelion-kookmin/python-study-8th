class calculator:
    def sum(self,num1, num2) :
        return num1 + num2
    def sub(self,num1, num2) :
        return num1 - num2
    def mul(self,num1, num2) :
        return num1 * num2
    def div(self,num1, num2) :
        return num1 / num2
    def quo(self,num1, num2) :
        return num1 // num2
    def remain(self,num1, num2) :
        return num1 % num2

cal = calculator()
print(cal.sum(1, 2))   
print(cal.sub(5, 3)) 
print(cal.mul(4, 3))
print(cal.div(100, 10))
print(cal.quo(10, 2))
print(cal.remain(10, 3))

