# https://www.codechef.com/practice


for i in range(int(input())):
    x, y, z = map(int, input().split())
    rem = (z - y)//x
    if  rem <= z:
        print(rem)