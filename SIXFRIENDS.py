# https://www.codechef.com/practice

T = int(input())
while T:
    A, B = input().split()
    dr = 3*int(A)
    tr = 2*int(B)
    leastcost = min(dr,tr)
    print(leastcost)
    T=T-1
