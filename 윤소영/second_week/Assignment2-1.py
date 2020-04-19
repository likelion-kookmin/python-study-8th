inputed_star=int(input("별피라미드 높이를 입력해주세요 -> "))   # 변수 = int(input()) ex) 5 -> inputed_star = 5
for i in range(inputed_star) :  # 입력받은 값이 list가 된다. ex) 5 -> [0,1,2,3,4] -> i
                print(" "*(inputed_star-1-i)+("*"*(2*i+1)))