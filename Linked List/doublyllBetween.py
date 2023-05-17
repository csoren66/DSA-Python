class Node:
    def __init__(self, data):
        self.data = data
        self.head = None

    def insertAfter(self, next_node, new_data):
        if next_node is Node:
            print("This Node doesn't exist in DLL")
            return
    
        new_node = Node(data=new_data)

        new_node.prev = next_node.prev

        next_node.prev = new_node

        new_node.next = next_node

        if new_node.prev is not None:
            new_node.prev.next = new_node

        else:
            head = new_node