# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                tree = []


        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                height = [0] * len(self.parent)
                for v in range(self.n):
                        height1 = 0
                        if self.parent[v] == -1 :
                                root = v
                        i = v
                        while i != -1:
                                if (height[i] != 0):
                                        height[v] = height[i] + height[v]
                                        break
                                else:
                                        height[v] = height[v] + 1
                                        i = self.parent[i]

                        maxHeight = max(maxHeight, height[v]);
                return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
