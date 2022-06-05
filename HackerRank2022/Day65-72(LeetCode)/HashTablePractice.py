# class HashTable:
#     """
#     A hash table with `capacity` buckets
#     that accepts string keys
#     """
#
#     def __init__(self, capacity):
#         self.capacity = capacity  # Number of buckets in the hash table
#         self.storage = [None] * capacity
#         self.item_count = 0
#
#     def get_num_slots(self):
#         """
#         Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table,
#         but the number of slots in the main list.)
#         One of the tests relies on this.
#         """
#         return len(self.storage)
#
#     def djb2(self, key):
#         """
#         DJB2 hash, 32-bit
#         """
#         # Cast the key to a string and get bytes
#         str_key = str(key).encode()
#
#         # Start from an arbitrary large prime
#         hash_value = 5381
#
#         # Bit-shift and sum value for each character
#         for b in str_key:
#             hash_value = ((hash_value << 5) + hash_value) + b
#             hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits
#
#         return hash_value
#
#     def hash_index(self, key):
#         """
#         Take an arbitrary key and return a valid integer index within the hash table's storage capacity.
#         """
#         return self.djb2(key) % self.capacity
#
#     def put(self, key, value):
#         """
#         Store the value with the given key.
#         """
#         index = self.hash_index(key)
#         self.storage[index] = value
#         return
#
#
#     def delete(self, key):
#         """
#         Remove the value stored with the given key.
#         Print a warning if the key is not found.
#         """
#         index = self.hash_index(key)
#         self.storage[index] = None
#
#
#     def get(self, key):
#         """
#         Retrieve the value stored with the given key.
#         Returns None if the key is not found.
#         """
#         index = self.hash_index(key)
#         return self.storage[index]
#
#
# a = HashTable(10)
# a.djb2(2)
#
# print(a.djb2(2))
# print(a.hash_index(2))
# print(a.put(7, 100))
# print(a.get(7))
# print(a.delete(7))
# print(a.get(7))
# print(a.put(7, 100))
# print(a.get(7))
# print(a.hash_index(7))
#
# bb = []
# if not bb:
#     print('hello')
#
# from collections import deque
#
# a = [1, 2, 3, 4, 5]
# d = 4
#
# list_deque = deque(a)
# for i in range(d):
#     item = list_deque.popleft()
#     print(item)
#
# count = 10
#
# while count > 1:
#     if count - 3 == 0:
#         print('hello')
#         break
#     print('jew')
#     break
#
# from collections import deque
#
# stack = deque()
# if not stack:
#     print('stack1')
# stack.append(1)
# if stack:
#     print('stack2')
#
# s = '{[()]}'
# s = '{[(])}'
# # {{[[(())]]}}
#
#
# stack = deque()
# for item in s:
#     # print(item)
#     if item == '(' or item == '[' or item == '{':
#         print(item)
#         stack.append(item)
#     elif item == ')':
#         a = stack.pop()
#         if a != '(':
#             print('NO')
#     elif item == ']':
#         b = stack.pop()
#         if b != '[':
#             print('NO')
#     elif item == '}':
#         c = stack.pop()
#         if c != '{':
#             print('NO')
# print(stack)
# print('YES')
#
# stack2 = deque()
# stack2.append(2)
# print(stack2[0])
#
# dict1 = {1: [1,2]}
# print(dict1[1])
#
# a = [2]
#
# for i in a:
#     if i < 2:
#         print('less than 2')
#     else:
#         print('is 2')
#     if i == 2:
#         print('i said it is 2')

# n = 10
# arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
#
# out_of_order = arr[-1]
# index = n-2
# while out_of_order < arr[index] and index:
#     temp = arr[index]
#     arr[index+1] = temp
#     print(*arr)
#     arr[index] = out_of_order
#     index -= 1
#     print(index)
# if arr[0]>arr[1]:
#     temp = arr[1]
#     arr[1] = arr[0]
#     print(*arr)
#     arr[0] = temp
#
#
# print(*arr)
#
# print("------------------------------------------------")
#
# n = 10
# arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
#
# target = arr[-1]
# idx = n - 2
#
# while (target < arr[idx]) and (idx >= 0):
#     arr[idx + 1] = arr[idx]
#     print(*arr)
#     idx -= 1
#     print(idx)
#
# arr[idx + 1] = target
# print(*arr)

# from collections import deque
#
# s='({)}]}[}]{({))}{)]()(](])})][(]{}{({{}[]{][)){}{}))]()}((][{]{]{][{}[)}}{)()][{[{{[[{-truncated-}'
# stack = deque()
# for item in s:
#     print(item)
#     if not stack:
#         if item == ')' or item == ']' or item == '}':
#             print('no')
#     if item == '(' or item == '[' or item == '{':
#         stack.append(item)
#     elif item == ')':
#         if stack.pop() != '(':
#             print('no')
#     elif item == ']':
#         if stack.pop() != '[':
#             print('no')
#     elif item == '}':
#         if stack.pop() != '{':
#             print('no')

from queue import Queue

class Node():
    def __init__ (self):
        self.distance = -1
        self.children = []
        self.visited = False
        self.name = 0

def bfs(numberOfNodes, numberOfEdges, edges, startNodeNumber):
    nodes = [Node() for _ in range(numberOfNodes)]
    for count, node in enumerate(nodes, 1):
        node.name = count
    for edge in edges:
        u, v = [nodes[i-1] for i in edge]
        u.children.append(v)
        v.children.append(u)
    for node in nodes:
        print(f'node = {node.name}; children = {[node.name for node in node.children]}')
    startNode = nodes[startNodeNumber-1] # getting index representation of the startNodeNumber and then setting that node as the start node
    startNode.distance = 0 # it doesn't have distance from itself and it is reachable by start node which means it is not -1
    queue = Queue()
    queue.put(startNode)
    iteration = 1
    while not queue.empty():
        print('\n\n')
        print(f'      ITERATION NUMBER = {iteration}')
        node = queue.get()
        print(f'      NODE IS = {node.name}')
        for child in node.children:
            print(f'pre test child name = {child.name}')
            if not child.visited:
                print('----->CHILD NOT VISITED<-----')
                print(f'post test child name = {child.name}')
                print(f'node distance = {node.distance}')
                print(f'child distance = {child.distance}')
                child.distance = node.distance + 6
                # print(f'------NODE DISTANCE IS = {node.distance}')
                print(f"------NODE {node.name}'S CHILD'S ({child.name}) DISTANCE IS NOW = {child.distance}")
                print('\n')
                child.visited = True
                queue.put(child)
        iteration += 1
    del nodes[startNodeNumber - 1]
    return [node.distance for node in nodes]

print(bfs(5, 2, [[1,2],[1,3],[3,4]], 1))




# first_multiple_input = input().rstrip().split()
# print(first_multiple_input)
# print(first_multiple_input[1])


edges = [[1, 2], [1, 3]]
nodes = [Node() for _ in range(4)]
for count, node in enumerate(nodes, 1):
    print(count)
    node.name = count
for edge in edges:
    u, v = [nodes[i-1] for i in edge]
    print(f'{u.name}<------->{v.name}')


'''FINISHED VERSION BFS

class Node:
    def __init__(self):
        self.distance = -1
        self.visited = False
        self.children = []
        self.name = ''

def bfs(numberOfNodes, numberOfEdges, edges, startNodeNumber):
    # Create the nodes
    nodes = [Node() for node in range(numberOfNodes)]
    # naming nodes for troubleshooting
    for count, node in enumerate(nodes, 1):
        node.name = count
    # labeling the start node
    startNode = nodes[startNodeNumber - 1]
    # start node's distance = 0 cus it is 0 away from itself (the reference point)
    startNode.distance = 0
    # creating the edges by looping through edges which are given in list format e.g.
    #  [1, 2] or [1, 3]
    for edge in edges:
        # cycle through nodes
        u, v = [nodes[i-1] for i in edge]
        u.children.append(v)
        v.children.append(u)
    queue = Queue()
    queue.put(startNode)
    while queue.qsize() > 0:
        # remove and return and item from the queue
        node = queue.get()
        for child in node.children:
            if not child.visited:
                child.visited = True
                child.distance = node.distance + 6
                queue.put(child)
    # return []
    del nodes[startNodeNumber-1]
    return [node.distance for node in nodes]

'''