inputed_star=int(input("숫자 입력 -> "))
for i in range(inputed_star) :  
    print(" "*(inputed_star-1-i)+("*"*(2*i+1)))
for i in range(inputed_star) : 
    if i == 0 :
        continue
    print(" "*i+("*"*(inputed_star*2-1-2*i)))