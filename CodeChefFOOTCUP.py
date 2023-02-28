# https://www.codechef.com/practice

t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if x>=1 and y>=1 and x==y:
        print("YES")
    else:
        print("NO")