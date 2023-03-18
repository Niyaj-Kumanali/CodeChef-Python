# https://www.codechef.com/practice


T = int(input())
while T:
    A, B, C = input().split()
    A=int(A)
    B=int(B)
    C=int(C)
    if C%A==0 and C%B==0:
        print("Any")
    elif C%A==0:
        print("Chicken")
    elif C%B==0:
        print("Duck")
    else:
        print("None")
  
    T=T-1
