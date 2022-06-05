class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()
print(llist)

first_node = Node('a')
llist.head = first_node
print(llist)

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node

print(first_node.next)
print(second_node.next)

print(llist)

# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
#     def __str__(self):
#         return '__str__ for car'
#
#     def __repr__(self):
#         return '__repr__ for Car'

print(list(reversed(range(1,11))))

d = dict()

d['a'] = 8

print(d)

# fruit_info = to_dict( 'fruit': 'apple', 'count': 2, 'price': 3.5 )
#
# print(fruit_info)

num_list = [1, 2, 3, 4, 5]
num_list.remove(2)
print(num_list)