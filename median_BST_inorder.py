def findMedian(root):
    d = []
    def inorder(r):
        if r:
            inorder(r.left)
            d.append(r.data)
            inorder(r.right)
    inorder(root)
    length = len(d)
    mid = length // 2
    if length % 2 == 0:
        sum = d[mid - 1] + d[mid]
        if sum % 2 == 0:
            return sum // 2
        else: return sum / 2
    else:
        median = d[mid]
        return median
    return

'''
For inorder traversal
You traverse the left subtree
You traverse
the root node
You tranverse the right subtree
'''
