#Uses python3

import sys
def greater(p ,q):
    for i in range(0,4):
        if p+q> q+p:
            return True

def largest_number(a):
    #write your code here
    for i in range(0,len(a)-1):
        for j in range(i+1, len(a)):
            if greater(a[j],a[i]):
                t= a[i]
                a[i] = a[j]
                a[j] = t

    res = ""
    for x in a:
        res= res +x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
