# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):        
        memory = {}        
        for i, e in enumerate(inorder):
            memory[e] = i
            
        root = self.helper(preorder[::-1], inorder, 0, len(inorder), memory)        
        return root

    
    def helper(self, preorder, inorder, leftPointer, rightPointer, memory):        
        if leftPointer >= rightPointer: 
            return None
        
        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)
        
        root.left = self.helper(preorder, inorder, leftPointer, idx, memory)
        root.right = self.helper(preorder, inorder, idx+1, rightPointer, memory)
        
        return root       
        