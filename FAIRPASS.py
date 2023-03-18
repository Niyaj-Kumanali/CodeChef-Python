# https://www.codechef.com/practice


# Program to check whether no of persons can enter with available passes
t= int(input())
while t:
    n, k = map(int, input().split())
    if k>n:
        print("YES")
    else:
        print("NO")
    t-=1


