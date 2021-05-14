#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def order(node):
  if node == -1:
    return
  order(tree[node][1])
  result.append(node)
  order(tree[node][2])
  return result

def IsBinarySearchTree(tree):
  if len(tree)> 0:
    global result
    result = []
    order(0)
    for i in range(len(result)-1):
      if tree[result[i+1]][0] < tree[result[i]][0]:
        return False
      if tree[result[i+1]][0] == tree[result[i]][0] and tree[result[i+1]][1] == result[i]:
        return False
  # Implement correct algorithm here
  return True



def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
