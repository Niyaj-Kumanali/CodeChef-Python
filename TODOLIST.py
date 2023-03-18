# https://www.codechef.com/practice


t =int(input())
while t:
    count = 0
    n = int(input())
    d = list(map(int, input().split()))
    for i in d:
        if i >= 1000:
            count+=1
    t -= 1
    print(count)