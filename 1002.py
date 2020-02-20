def chk(x1, y1, r1, x2, y2, r2):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    else:
        if d == r1 + r2 or d == abs(r1-r2):
            return 1
        elif d > r1 + r2 or d < abs(r1-r2) or d == 0:
            return 0
        elif d < r1 + r2 and d > abs(r1-r2):
            return 2


T = int(input())
for i in range(0, T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(chk(x1, y1, r1, x2, y2, r2))

