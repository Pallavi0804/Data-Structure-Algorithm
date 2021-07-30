# https://www.youtube.com/watch?v=lFq5mYUWEBk
# https://www.youtube.com/watch?v=JnrbMQyGLiU

#Insert, Serach, Delete and Inorder, Preorder, postorder Traversal Operations

class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self,data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self,k):
        if self.data == k:
            return True
        if k < self.data:
            if self.left:
                return self.left.search(k)
            else:
                False
        else:
            if self.right:
                return self.right.search(k)
            else:
                False

    def my_delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
                if self.left == None:
                    return True
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
                if self.right == None:
                    return True
        else:
            if self.left == None and self.right == None:
                return None
            elif self.left == None:
                return self.right
            elif self.right == None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return False


    def delete(self,val):
        if val < self.data:
            #if val is in left subtree
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            #if val is in right subtree
            if self.right:
                self.right = self.right.delete(val)
        else:
            # if val is self.data
            if self.left == None and self.right == None:
                return None
            elif self.left == None:
                return self.right
            elif self.right == None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data,end=' ')
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data,end=' ')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.data,end=' ')

def Build_Tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.addchild(elements[i])
    return root


if __name__ == '__main__':
    # String Tree
    str_tree = ["Pallavi","Pravin","Nitin","Megha","kalpana","Balraj"]
    # Number Tree
    num_tree = [17, 4, 1, 20, 9, 23, 18, 34]
    num_root = Build_Tree(num_tree)
    str_root = Build_Tree(str_tree)

    # Serach node
    int_k = 25
    str_k = "Pallavi"
    if str_root.search(str_k):
        print(str_k," is Present in Tree")
    else:
        print(str_k," is not present in Tree")

    # Printing in inorder, preorder and postorder
    print("\nInorder Traversal ",end=' ')
    num_root.inorder_traversal()
    print("\nPreorder Traversal ", end=' ')
    num_root.preorder_traversal()
    print("\nPostorder Traversal ", end=' ')
    num_root.postorder_traversal()

    # Delete node
    '''del_val = 20
    #num_root.delete(del_val)
    if num_root.my_delete(del_val) == True:
        print("\nInorder after deleting ",del_val)
        num_root.inorder_traversal()
    else:
        print("Node ",del_val," is not present in tree to delete")'''

    num_root.delete(9)
    print("\nInorder after delete ")
    num_root.inorder_traversal()





