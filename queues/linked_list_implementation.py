class Node:
     
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
     
    def __init__(self):
        self.front = None 
        self.rear = None
 
    def is_empty(self):
        return self.front == None
     
    def enqueue_operation(self, item):
        current_node = Node(item)
         
        if self.rear == None:
            self.front = self.rear = current_node
            return
        self.rear.next = current_node
        self.rear = current_node
 
    def dequeue_operation(self):
         
        if self.is_empty():
            return
        current_node = self.front
        self.front = current_node.next
 
        if(self.front == None):
            self.rear = None
