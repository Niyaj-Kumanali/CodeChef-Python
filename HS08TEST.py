# https://www.codechef.com/practice

x, y = map(float, input().split())
x = int(x)
if x % 5 == 0 and x+0.5 <= y:
    print(float(y-x-0.50))
else:
    print(float(y))