def insertion_sort(self):
    if self.length < 2:
        return
    
    sorted_head = self.head
    current = self.head.next
    sorted_head.next = None
    
    while current:
        next_node = current.next
        
        # Insert at beginning
        if current.value < sorted_head.value:
            current.next = sorted_head
            sorted_head = current
        else:
            # Find insertion point
            search = sorted_head
            while search.next and search.next.value < current.value:
                search = search.next
            current.next = search.next
            search.next = current
        
        current = next_node
    
    self.head = sorted_head
    # Update tail
    temp = self.head
    while temp.next:
        temp = temp.next
    self.tail = temp
