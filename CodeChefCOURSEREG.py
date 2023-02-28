# https://www.codechef.com/practice

for i in range(int(input())):
    n, m, k = map(int, input().split())
    if m - k >= n:
        print('YES')
    else:
        print("NO")