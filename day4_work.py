class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def traverse(self):
        node = self
        while node is not None:
            print(node.value)
            node = node.next
            
            
node1 = LinkedListNode('January')
node2 = LinkedListNode('February')
node3 = LinkedListNode('April')

node1.next = node2
node2.next = node3

node1.traverse()
#January
#February
#April
# Complete Implementation of Linked List
# - Add new node to the front of the linked list
# - Add new node to the end of the linked list
# - Get a node by its value
# - Insert new node after a particular node
# - Traverse through the linked list and print values


# 2 Classes - Node Class and Linked List Class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"<Node|{self.value}>"
    
    
class LinkedList:
    def __init__(self, head_node=None):
        # head attribute will point to the first node of the Linked List
        self.head = head_node
        
    # Method to add a new node to the beginning of the linked list
    def push_on(self, new_value): # O(1) - Constant Time 
        # Create a new node with the value passed in
        new_node = Node(new_value)
        # Set the new_node's .next attribute to be the current head
        new_node.next = self.head
        # Set the head of the linked list to the new node
        self.head = new_node
        
    # Method to print out all of the nodes in the Linked List in order
    def print_list(self):
        # Start at the beginning of the list
        node = self.head
        # While the node is a node (and not None), continue to loop
        while node is not None:
            # Print the node (which will call the Node __str__ method)
            print(node)
            # Go to the next node in the list
            node = node.next
            
    # Method to add a new node to the end of the linked list
    def append(self, new_value): # O(n) - Linear Time
        # Create a new node with the value passed in
        new_node = Node(new_value)
        # Check if the linked is empty
        if self.head is None:
            # Set the head to be the new node
            self.head = new_node
        # If not empty
        else:
            # Traverse to the end of the list
            node = self.head
            while node.next is not None:
                # Move to the next node
                node = node.next
            # once the node.next IS None, set that node's .next to be the newly created node
            node.next = new_node

    def remove(self, key):
        current = self.head


        # If head node itself holds the key to be deleted 
        if current: 
            if current.value == key: 
                self.head = current.next
                current = None
                return
        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next' 
        while current: 
            if current.value == key: 
                break
            prev = current 
            current = current.next
        # if key was not present in linked list 
        if not current: 
            return
        # Unlink the node from linked list 
        prev.next = current.next
        current = None
            
    # Method to get a node by value or return None if not in the Linked List
    def get_node(self, value_to_get):
        # Start with the head
        node_to_check = self.head
        # while node_to_check is a node
        while node_to_check is not None:
            # Check if that is the node we are looking for
            if node_to_check.value == value_to_get:
                # Return that node
                return node_to_check
            # if not, move on to the next node
            node_to_check = node_to_check.next
        # Once the node to check is None, we know the value to get is not in the linked list
        return None
    
    # Method to insert a new node in the linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value):
        # Get the previous node by value
        prev_node = self.get_node(prev_value)
        # Make sure the node exists
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            # Create a new node with the new value
            new_node = Node(new_value)
            # point the new_node's .next attribute at the previous node's .next
            new_node.next = prev_node.next
            # point the prev_node's .next to the new node
            prev_node.next = new_node
            
            
    
        
        
months = LinkedList()
months.append('July')
months.append('August')
months.push_on('June')
months.push_on('March')
months.push_on('February')
months.append('September')
months.insert_after('March', 'April')
months.insert_after('April', 'May')
months.append('November')
months.insert_after('September', 'October')
months.append('December')
months.push_on('January')
months.print_list()