# https://www.codechef.com/practice

for i in range(int(input())):
    x, y = map(int, input().split())
    if (y/x*100) >= 107:
        print("YES")
    else:
        print("NO")