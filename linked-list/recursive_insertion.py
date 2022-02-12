# Insert recusrsively
from linked_list import LinkedList, Node

#! This code is not working for head insertion
def insert_recursive(node, head, data, index):
    if index == 0:
        new_node = Node(data)
        new_node.set_next(node)
        if node == head:
            head = new_node
        return new_node

    index -= 1
    node.set_next(insert_recursive(node.get_next(), head, data, index))
    return node

lst = LinkedList()
lst.add(10)
lst.add(20)
lst.add(30)
lst.add(40)
lst.add(50)

insert_recursive(lst.get_head(), lst.get_head(), 25, 1)
lst.display()
