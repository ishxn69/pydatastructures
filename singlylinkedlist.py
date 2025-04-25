class Node:
    
    def __init__(self, data):
        self.data = data #assign data
        self.next = None #initialize next as null

#Linked List class contains a Node object
class LinkedList:
    
    #initialise head
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def prepend(self, data):

        new_node = Node(data) #creating the new node
    
        if self.head == None: #linked list is empty
            self.head = new_node #give the head reference to the new node
        else:
            new_node.next = self.head #connect the new node to the linked list
            self.head = new_node #give the head reference to the new node
    
    def append(self,data):
        new_node = Node(data) #creating the new node
        
        if self.head == None: #linked list is empty
            self.head = new_node #give the head reference to the new node
        else:
            #traversing the linked list to find the last node
            curr = self.head
            #while curr.next is not None!
            #Otherwise curr will get assigned value 'None'
            #in the last step
            while curr.next != None:
                curr = curr.next
            curr.next = new_node #point the next element of the last node to the newly created node

    #Insert element into given position in a LinkedList
    def insert(self, data, position):
        new_node = Node(data)

        cur_node = self.head
        prev = None
        count = 0
        while cur_node != None and count < position:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        if cur_node != self.head:
            prev.next = new_node
            new_node.next = cur_node
        else:
            new_node.next = cur_node
            self.head = new_node

    #delete the first element of LinkedList
    def delete_first(self):
        if self.head == None:
            print("Empty Linked List")
        else:
            cur_node = self.head
            self.head = self.head.next
            del cur_node
    
    # Delete the last element of LinkedList        
    def delete_last(self):
        if self.head == None:
            print("Empty Linked List")
        else:
            cur_node = self.head
            prev = None
            while cur_node.next != None:
                prev = cur_node
                cur_node = cur_node.next
            prev.next = None
            del cur_node 

    #delete Element at a given position in a LinkedList
    def delete_position(self, position):
        if self.head == None:
            print("Empty Linked List")
        else:
            cur_node = self.head
            prev = None
            count = 0
            while cur_node != None and count < position:
                prev = cur_node
                cur_node = cur_node.next
                count += 1
            if cur_node == self.head:
                self.head = cur_node.next
                del cur_node
            else:
                prev.next = cur_node.next
                del cur_node
