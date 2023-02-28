# https://www.codechef.com/practice


# Progrma to find total no of chapters person has to study this semester
t = int(input())
while t:
    # x=courses y=units z=chapters
    x,y,z =map(int, input().split())
    print(x*y*z)
    t -= 1