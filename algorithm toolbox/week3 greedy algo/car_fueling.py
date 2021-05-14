# python3
import sys


def compute_min_refills(distance, tank, n, stops):
    # write your code here
    norefill=0
    current=0
    last = 0
    while current <= n:
        last = current
        while current <= n and (stops[current + 1] - stops[last] <= tank):
            current = current + 1

        if current == last:
            return -1
        if current <= n:
            norefill = norefill + 1

    return norefill

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    stops.insert(0,0)
    stops.insert(n+1, d)

    print(compute_min_refills(d, m, n, stops))
