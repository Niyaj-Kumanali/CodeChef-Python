# https://www.codechef.com/practice


# Program to determine whether he can buy 1kg of apples and oranges
x = int(input())
a,b = map(int,input().split())
if x>=a+b:
    print("YES")
else:
    print("NO")