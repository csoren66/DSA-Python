class Node:
    def __init__(self, data):
        self.data = data
        self.head = None

    def append(self, new_data):

        new_node = Node(data=new_data)
        last = self.head

        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while (last.next is not None):
            last = last.next

        last.next = new_node

        new_node.prev = last