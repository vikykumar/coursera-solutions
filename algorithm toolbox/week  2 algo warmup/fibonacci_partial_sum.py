# Uses python3
import sys

def fibonacci_partial_sum_naive( fr, to):
    x = []
    x.insert(0, 0)
    x.insert(1, 1)
    r = 60
    sum1 = 1
    sum2 = 1
    if to == 0:
        sum1 = 0
    elif to < r:
        for i in range(2, to + 1):
            x.insert(i, (x[i - 1] + x[i - 2]) % 10)
            sum1 = sum1 + x[i]
    else:
        p = to % 60
        if p== 0:
            sum1 = 0
        else:
            for c in range(2, p + 1):
                x.insert(c, (x[c - 1] + x[c - 2]) % 10)
                sum1 = sum1 + x[c]
    d = []
    d.insert(0, 0)
    d.insert(1, 1)
    if fr == 0 or (fr - 1) == 0:
        sum2 = 0
    elif fr < r-1:
        for i in range(2, fr):
            d.insert(i, (d[i - 1] + d[i - 2]) % 10)
            sum2 = sum2 + d[i]
    else:
        p = (fr - 1) % 60
        if p== 0:
            sum2 = 0
        else:
            for c in range(2, p + 1):
                d.insert(c, (d[c - 1] + d[c - 2]) % 10)
                sum2 = sum2 + d[c]

    return (sum1 - sum2)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))