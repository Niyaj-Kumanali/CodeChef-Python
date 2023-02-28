# https://www.codechef.com/practice


t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    total = a + b + c
    if total >= 100 and a >= 10 and b >= 10 and c >= 10 :
        print("PASS")
    else:
        print("FAIL")