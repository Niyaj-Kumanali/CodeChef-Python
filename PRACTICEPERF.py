# https://www.codechef.com/practice


p = map(int,input().split())
count = 0
for i in p:
    if i >= 10:
        count += 1
print(count)