# https://www.codechef.com/practice


t = int(input())
a, b, c = 0, 0, 0
for i in range(0, t):
    (S, T) = map(int, input().split())
    a += S
    b += T
    if (a > b):
        d = a - b
        if (d > c):
            c = d
            w = 1
    else:
        e = b - a
        if (e > c):
            c = e
            w = 2
print(w, c)


