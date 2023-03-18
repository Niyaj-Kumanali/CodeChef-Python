# https://www.codechef.com/practice


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


t = int(input())
while t:
    fact = int(input())
    print(factorial(fact))
    t-=1