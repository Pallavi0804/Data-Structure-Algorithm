class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addchild(self,child):
        child.parent = self
        self.children.append(child)

    def getHeight(self,root):
        pass

    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self):
        spaces = ' ' * self.getlevel() * 3
        prefix = spaces + '|__'+self.data
        print(prefix)
        for child in self.children:
            if self.children:
                child.printTree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.addchild(TreeNode("Mac"))
    laptop.addchild(TreeNode("Surface"))
    laptop.addchild(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addchild(TreeNode("iPhone"))
    cellphone.addchild(TreeNode("Google Pixel"))
    cellphone.addchild(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.addchild(TreeNode("Samsung"))
    tv.addchild(TreeNode("LG"))

    root.addchild(laptop)
    root.addchild(cellphone)
    root.addchild(tv)

    return root
    

if __name__ == '__main__':
    root = build_product_tree()
    root.printTree()
    print("Height of the Tree")
    print(root.getHeight(root))

