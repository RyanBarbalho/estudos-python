# Write a Python program to create a class representing a linked list data structure.
# Include methods for displaying linked list data, inserting and deleting nodes.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self.insert_node(value, self.head)

    def insert_node(self, value, node):
        if node.next == None:
            node.next = Node(value)
        else:
            self.insert_node(value, node.next)

    def delete(self, value):
        if self.head == None:
            return False
        elif self.head.value == value:
            self.head = self.head.next
        else:
            self.delete_node(value, self.head)

    def delete_node(self, value, node):
        if node.next == None:
            return False
        elif node.next.value == value:
            node.next = node.next.next
        else:
            self.delete_node(value, node.next)

    def __str__(self):
        if self.head == None:
            return "[]"
        else:
            return self.display(self.head)

    def display(self, node):
        string = ""

        while node.next != None:
            string += f"{node.value} -> "
            node = node.next

        string += f"{node.value}"

        return string


def main():
    try:
        linked_list = LinkedList()
        linked_list.insert(1)
        linked_list.insert(2)
        linked_list.insert(3)
        linked_list.insert(4)
        linked_list.insert(5)
        print(linked_list)
        linked_list.delete(3)
        print(linked_list)
    except Exception as e:
        print("Erro: ", e)


if __name__ == "__main__":
    main()
