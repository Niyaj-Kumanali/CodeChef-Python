# https://www.codechef.com/practice

t = int(input())
for i in range(t):
    k,x = map(int, input().split())
    if x<k:
        print(k-x)

