# https://www.codechef.com/practice


# program to check required extra seats for math course
t = int(input())
while t:
    # x-> seats y->students
    x, y = map(int, input().split())
    if x>=y:
        print("0")
    else:
        print(y-x)

    t-=1