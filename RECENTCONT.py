# https://www.codechef.com/practice


t = int(input())
while t:
    s = 0
    l = 0
    n = int(input())
    code = list(input().split())
    for i in code:
        if i == "START38":
            s+=1
        else:
            l += 1
    t -= 1
    print(s, l)

# 4
# 3
# START38 LTIME108 START38
# 4
# LTIME108 LTIME108 LTIME108 START38
# 2
# LTIME108 LTIME108
# 6
# START38 LTIME108 LTIME108 LTIME108 START38 LTIME108

