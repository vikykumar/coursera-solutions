#Uses python3
import sys
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def minimum_distance(cord):
    m = len(cord) // 2
    if m == 1:
        return naive(cord)

    mid = cord[m][0]
    d1 = minimum_distance(cord[:m])
    d2 = minimum_distance(cord[m:])
    d = min(d1, d2)
    d3 = split(cord,d)
    #write your code here
    return min(d,d3)

def split(coord, ds):
    p = []
    m = len(coord)//2
    mid = coord[m][0]
    for c in coord:
        if abs(c[0] - mid) < ds :
            p.append(c)
    p.sort(key=lambda pi: pi[1])
    if len(p) < 2:
        return ds
    else:
        ds1 = dist(p[0], p[1])
        for i in range(len(p) - 1):
            for j in range(i + 1, min(i + 7, len(p))):
                ds1 = min(ds1, dist(p[i], p[j]))
        return ds1

def naive(ax):
    mi = dist(ax[0], ax[1])
    ln_ax = len(ax)
    if ln_ax == 2:
        return mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:  # Update min_dist and points
                    mi = d
    return mi

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
    points.sort()
 #   print(points)
    d1 = minimum_distance(points)
    print("{0:.9f}".format(d1))
