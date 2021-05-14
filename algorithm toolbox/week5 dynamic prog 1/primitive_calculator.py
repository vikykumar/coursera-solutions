# Uses python3
import sys


def optimal_sequence(n):
    no_of_op = [float("inf")]*(n+1)
    no_of_op[0:2] = 0, 0

    for i in range(2,n+1):
        t1, t2 = float("inf"), float("inf")
        if i%2 == 0:
            t1 = no_of_op[int(i/2)]
        if i%3 == 0:
            t2 = no_of_op[int(i/3)]
        no_of_op[i] = min(t1,t2,no_of_op[i-1]) + 1
   # print("jfds",no_of_op)
    sequece = [n]
    i = n
    while i > 1:
        if i % 2 == 0 and no_of_op[i] == no_of_op[int(i / 2)] + 1:
            i = int(i / 2)
            sequece.append(i)
        elif i % 3 == 0 and no_of_op[i] == no_of_op[int(i / 3)] + 1:
            i = int(i / 3)
            sequece.append(i)
        else:
            i = i - 1
            sequece.append(i)

    return sequece


n = int(input())
seq = optimal_sequence(n)
print(len(seq)-1)
for x in reversed(seq):
    print(x, end = ' ')
