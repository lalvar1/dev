from collections import deque
from binarytree import bst, heap
from queue import LifoQueue
import sys

class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        # Stack for DFS
        stack = LifoQueue()
        # Put the root node
        stack.put((A,1))
        # Initialize mindepth to a large value
        mindepth = sys.maxsize
        # While the stack is not empty
        while not stack.empty():
            # Get the node and the depth
            node, depth = stack.get()
            # Push left and right children and their depths to the stack (if they exist)
            if node.left is not None:
                stack.put((node.left, depth+1))
            if node.right is not None:
                stack.put((node.right, depth+1))
            # If the popped node is a leaf node and has lesser depth than mindepth then update mindepth
            if node.left is None and node.right is None:
                if depth<mindepth:
                    mindepth = depth
        return mindepth

def minDepth(A):
    q = deque()
    q.append(A)
    curr, nest, level = 1, 0, 1
    while q:
        item = q.popleft()
        curr -= 1
        if not item.right and not item.left:
            return level
        if item.right:
            q.append(item.right)
            nest += 1
        if item.left:
            q.append(item.left)
            nest += 1
        if curr == 0:
            curr, nest = nest, curr
            level += 1

a = bst()
print(a)
#a= {3, 1, -1, -1}
print(minDepth(a))
b = heap()
print(b)