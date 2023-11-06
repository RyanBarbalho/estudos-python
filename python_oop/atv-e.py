# Write a Python program to create a class representing a binary search tree.
# Include methods for inserting and searching for elements in the binary tree.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_node(value, self.root)

    def insert_node(self, value, node):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self.insert_node(value, node.left)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self.insert_node(value, node.right)

    def search(self, value):
        if self.root == None:
            return False
        else:
            return self.search_node(value, self.root)

    def search_node(self, value, node):
        if node == None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self.search_node(value, node.left)
        else:
            return self.search_node(value, node.right)


def main():
    try:
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(2)
        tree.insert(7)
        tree.insert(12)
        tree.insert(17)
        print(tree.search(10))
        print(tree.search(5))
        print(tree.search(15))
        print(tree.search(2))
        print(tree.search(7))
        print(tree.search(12))
        print(tree.search(17))
        print(tree.search(1))
        print(tree.search(3))
        print(tree.search(6))
        print(tree.search(8))
        print(tree.search(11))
        print(tree.search(13))
        print(tree.search(16))
        print(tree.search(18))
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
