# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyhash(text):
    ans = 0
    for c in reversed(text):
        ans = (ans * 263 + ord(c)) % 100000000007
    return ans

def precomputehash(text,pattern):
    t = len(text)
    p = len(pattern)
    h = [0]*(t-p+1)
    s = text[t-p:]
    h[t-p] = polyhash(s)
    y = 1
    for i in range(1,p +1):
        y = (y * 263) % 100000000007
    for i in reversed(range(t-p)):
        h[i] = (263*h[i+1] + ord(text[i]) - y*ord(text[i+p])) % 100000000007
    return h


def get_occurrences(pattern, text):
    result = []
    pt = polyhash(pattern)
    c = len(text) - len(pattern)
    st = precomputehash(text, pattern)
    for i in range( c + 1):
        if i == c  :
            p = text[i:]
        else :
            p = text[i:i+len(pattern)]
        if pt == st[i] and pattern == p:
                result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

