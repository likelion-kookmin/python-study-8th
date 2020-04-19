inputed_star=int(input("별역삼각형 높이를 입력해주세요 -> "))
for i in range(inputed_star) : 
    print(" "*i+("*"*(inputed_star*2-1-2*i)))