# https://www.codechef.com/practice


for i in range(int(input())):
    w, x, y, z = map(int, input().split())
    fill = w + (y*z)
    if fill > x:
        print("OVERFLOW")
    elif fill == x:
        print("FILLED")
    else:
        print("UNFILLED")