#node of doubly linked list    
class Node:    
    def __init__(self, data):    
        self.data = data;    
        self.previous = None    
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse(self):    
        #Node current will point to head    
        current = self.head   
        if self.head == None:    
            print("List is empty")  
            return  
        print("Nodes of doubly linked list: ")    
        while current != None:     
            #prints each node by incrementing pointer   
            print(current.data)  
            current = current.next

    def append(self, data):    
        new_node = Node(data)   
            
        if self.head == None:    
            self.head = self.tail = new_node    
            self.head.previous = None  
            self.tail.next = None    
        else:    
            self.tail.next = new_node    
            new_node.previous = self.tail  
            self.tail = new_node    
            self.tail.next = None 
            
    def delete_first(self):
        if self.head == None:
            return
        
        else:
            if self.head != self.tail:
                self.head = self.head.next
                self.head.previous = None
            #If we are here, this means there's only 1 element.
            else:
                self.head = self.tail = None
