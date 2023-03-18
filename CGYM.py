# https://www.codechef.com/problems/CGYM


for i in range(int(input())):
    x, y, z = map(int, input().split())
    if x <= z and z < x+y:
        print(1)
    elif z >= x + y:
        print(2)
    else:
        print(0)