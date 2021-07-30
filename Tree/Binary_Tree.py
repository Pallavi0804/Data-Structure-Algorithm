class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def PrintTree(self):
        print(self.data)

root = Node(10)
root.PrintTree()
