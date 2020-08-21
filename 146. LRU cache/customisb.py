
""" 
Python3 program to check if Binary tree is 
height-balanced 
"""
  
# A binary tree node 
class Node: 
      
    # constructor to create node of  
    # binary tree 
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None
  
# utility class to pass height object 
def checkHeight(root):
    
    if root==None:
        return 0
    lh=checkHeight(root.left)
    rh=checkHeight(root.right)
    print(lh,rh,root.data)
    if lh==-1:
        return False
    if rh==-1:
        return False
    heightdiff=lh-rh

    if abs(heightdiff)>1:
        return False
    else:
        return max(lh,rh)+1
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
#root.right.left = Node(6) 
root.left.left.left = Node(7)


#          1 
#         / \ 
#        2    3 
#       / \   / 
#      4   5 6  
#     7  
if checkHeight(root): 
    print('Tree is balanced') 
else: 
    print('Tree is not balanced') 
