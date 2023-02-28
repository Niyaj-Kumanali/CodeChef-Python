# https://www.codechef.com/practice

t = int(input())
while t:
    count = 0
    l, r = map(int, input().split())
    for i in range(l, r+1):
        rem = i % 10
        if rem == 2 or rem == 3 or rem == 9:
            count += 1
    print(count)
    t -= 1
