# python3

import sys

def hashtable(text, prime, x):
	h = [0]*(len(text)+1)
	h[0] = 0
	for i in range(1,len(text)+1):
		h[i] = (x*h[i-1] + ord(text[i-1]))%prime
	return h

def subhash(h,a,l,m):
	y = pow(263, l , m)
	subh = (h[a+l] - y*h[a])%m
	return subh

s = sys.stdin.readline()
q = int(sys.stdin.readline())
m1 = 10000000007
m2 = 10000000009
h1 = hashtable(s,m1,263)
h2 = hashtable(s,m2,263)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	a1 = subhash(h1,a,l,m1)
	a2 = subhash(h2,a,l,m2)
	b1 = subhash(h1,b,l,m1)
	b2 = subhash(h2,b,l,m2)
	print("Yes" if a1==b1 and a2==b2 else "No")
