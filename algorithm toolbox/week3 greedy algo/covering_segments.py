# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    print(segments)

    return points




if __name__ == '__main__':
    inp = int(input())
    seg = []
    points = []
    for i in range(inp):
        time = sys.stdin.readline()
        seg.append(list(map(int, time.split())))
    seg.sort()
    mn = seg[0][0]
    mx = seg[0][1]
    for i in range(inp-1):
        mn1 = max(mn, seg[i+1][0])
        mx1 = min(mx, seg[i+1][1])
        if mx1 < mn1:
            points.append(max(mn, mx))
            mn = seg[i+1][0]
            mx = seg[i+1][1]
        else:
            mn = mn1
            mx = mx1
    points.append(max(mn, mx))
    print(len(points))
    for i in points:
        print(i, end=" ")
