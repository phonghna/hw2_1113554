# question1.py
# 湖阮英風
# 1113554
# Date of Submission: TBD

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes):
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes):
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

def diamter(root):
    #inintialize diamter
    d = 0

    def dfs(node):
        nonlocal d
        if node == None:
            return 0

        #compute the height of the left and right subtrees
        left_height = dfs(node.left)
        right_height = dfs(node.right)

        #update the d to include the longest path through this node
        d = max(d, left_height + right_height)

        #return the height of the subtree rooted at this node
        return 1 + max(left_height, right_height)

    dfs(root)
    return d

#READ THIS: if you are lazy to type the input then comment all the lines inside "input zone" and uncomment the "lazy input"

#------INPUT ZONE---------
num = input("Enter your sequence of nodes: ")

nodes = list(map(int, num.split()))

#-----INPUT ZONE----------

#------LAZY INPUT---------
#nodes = [1, 2, 3, 4, 5, -1, -1, -1, -1, 6, 7]
#-----LAZY INPUT---------

root = tree(nodes)
#print(root)
print(diamter(root))  
