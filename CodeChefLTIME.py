# https://www.codechef.com/practice

# program to check wheather its lunch time or not
t=int(input())
while t:
    x = int(input())
    if x in range(1,5):
        print("YES")
    else:
        print('NO')
    t-=1