# https://www.codechef.com/practice


# program to determine whether he has enough money to buy a burger for each of his friends of not
t=int(input())
while t:
    # n = no of friends x= cost of each burger k=total money
    n,x,k = map(int, input().split())
    if k >= n*x:
        print("YES")
    else:
        print("NO")
    t-=1