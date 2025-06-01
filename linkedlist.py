class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addnode_beginning(self, data):
        new_node = Node(data)
        if self.head:  # If list is not empty
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def addnode_end(self, data):
        new_node = Node(data)
        if self.head:  # If list is not empty
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def middle(self):
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        if slow:
            print("Middle node data:", slow.data)
        else:
            print("The list is empty.")
            
    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next       # Save next
            current.next = prev      # Reverse link
            prev = current           # Move prev
            current = nxt            # Move current forward
        self.head = prev             # New head
   
   
    def Rotate(self):
        if not self.head or not self.head.next:
            return
    
        current = self.head
        prev = None

        while current.next:
            prev = current
            current = current.next
    
        self.addnode_beginning(current.data)  
        
    def del_from_sorted_linked_list(self) :
        current = self.head
        while current.next :
            if current.data == current.next.data :
                return current.next
            
            
            current=current.next 
            


                
            
        





                 
        
        
            
      