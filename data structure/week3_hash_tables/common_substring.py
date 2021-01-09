# python3

import sys
from collections import namedtuple

Answer = namedtuple('Answer', 'p q len')
def PolyHash(sa, m):
    hash_value = 0
    for i in reversed(range(len(sa) )):
        hash_value = (hash_value * 263 + ord(sa[i])) % m
    return hash_value

def hashdict(sb, l1, m):
    D = {}
    subs = sb[len(sb) - l1:]
    last = PolyHash(subs, m)
    D[last] = len(sb) - l1
    y = pow(263, l1, m)
    for j in reversed(range(len(sb) - l1 )):
        current = (263 * last + ord(sb[j]) - y * ord(sb[j +l1 ])) % m
        D[current] = j
        last = current
    return D


def hashtable(sa, l2, m):
    h = [0]*(len(sa) - l2 +1)
    h[len(sa) - l2] = PolyHash(sa[len(sa) - l2:],m)
    y = pow(263, l2, m)
    for i in reversed(range(len(sa) - l2 )):
        h[i] = (263 * h[i + 1] + ord(sa[i]) - y * ord(sa[i + l2 ])) % m
    return h


def solve(a,b,low,high,max,ast,bst ):
    t_s = (low + high)//2
    if low > high:
        return Answer(ast, bst, max)
    a1 = hashtable(a, t_s, m1)
    a2 = hashtable(a, t_s, m2)
    b1 = hashdict(b, t_s, m1)
    b2 = hashdict(b, t_s, m2)
    for i in range( len(a1)):
        temp1 = b1.get(a1[i], -1)
        temp2 = b2.get(a2[i], -1)
        if temp1 != -1 and temp2 != -1:
            max = t_s
            ast, bst = i , temp1
            del a1, a2, b1, b2
            return solve(a,b,t_s+1,high,max,ast,bst)
    return solve(a,b,low,t_s-1,max,ast,bst)


#for line in sys.stdin.readlines():
while True:
    line = sys.stdin.readline()
    m1 = 10000000007
    m2 = 10000001019
    x = 263
    try :
        s, t = line.split()
    except :
        break
    ans1 = Answer(0, 0, 0)
    if len(s) > len(t) :
        ans = solve(t,s,0,len(t),0,0,0)
        print(ans.q, ans.p, ans.len)
    else :
        ans = solve(s,t,0,len(s),0,0,0)
        print(ans.p, ans.q, ans.len)
