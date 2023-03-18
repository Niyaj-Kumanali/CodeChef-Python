# https://www.codechef.com/practice


n = int(input())
a = map(int, input().split())
even = odd = 0
for i in a:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")