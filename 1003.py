def fibonacci(N):
    if N == 2:
        return 1, 1
    current = 0
    prev_prev = 1
    prev = 1
    for i in range(3, N+1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    return prev_prev, current


T = int(input())
for i in range(0, T):
    N = int(input())
    if N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')
    else:
        cnt_zero, cnt_one = fibonacci(N)
        print(cnt_zero, cnt_one)
