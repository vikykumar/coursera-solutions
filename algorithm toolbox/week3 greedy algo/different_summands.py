# Uses python3
import sys

def optimal_summands(n):
    summands = []
    i=0
    while n != 0:
        if n-i-1> i+1:
            summands.append(i+1)
            n= n-i-1
            i=i+1
        else:
            summands.append(n)
            n = 0


    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
