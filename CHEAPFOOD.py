# https://www.codechef.com/practice


T = int(input())
while T:
    A= input()
    A = int(A)
    ten = A*10//100
    hundred = 100   
    if ten > hundred:
        print(ten)
    else:
        print(hundred)
    T=T-1
