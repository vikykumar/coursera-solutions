import sys
from _collections import deque

def hashTable(s, prime, x):
    h = list([] for _ in range(len(s) + 1))
    h[0] = 0
    for i in range(1, len(s) + 1):
        h[i] = (h[i - 1] * x + ord(s[i - 1])) % prime
    return h

def subhash(table, start, length):
    y = pow(x, length, pr)
    hash_value = (table[start + length] - y * table[start]) % pr
    return hash_value

def nextmsm(i, len, lenp,k):
    st = deque()
    st.append((i, 0, len, 1))
    st.append((i + len, len, lenp - len, 1))
    count = 0
    temp = 2
    C = 0
    while st:
        a, b, L, n = st.popleft()
        u1 = subhash(tx, a, L)
        v1 = subhash(pt, b, L)
        if temp != n:
            count = C
        if u1 != v1:
            count += 1
            if L > 1:
                st.append((a, b, L // 2, n + 1))
                st.append((a + L // 2, b + L // 2, L - L // 2, n + 1))
            else:
                C += 1
        if count > k:
            return False
        temp = n
    if count > k:
        return False
    else:
        return True


def solve(o, text, pattern):
    global tx, pt
    pos = []
    tx = hashTable(text, pr, x)
    pt = hashTable(pattern, pr, x)
    for i in range(len(text) - len(pattern)+1):
        if nextmsm(i, len(p)//2, len(p), o):
            pos.append(i)

    return pos


pr = 1000000007
x = 263
while True:
    line = input()
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)

