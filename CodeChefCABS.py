# https://www.codechef.com/practice


# code to check the cheaper crab out ot two prices
T = int(input())

while T:
    X, Y = map(int, input().split())
    if X < Y:
        print("FIRST")
    elif X==Y:
        print("ANY")
    else:
        print("SECOND")
    T-=1