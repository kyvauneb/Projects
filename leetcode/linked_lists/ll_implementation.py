# Linked Lists
# Pros
## Dynamic - can grow and shrink as needed
## No wasted memory - arrays allocate blocks of memory so as to facilitate indexed access via position + offset
## Insertions and Deletions are straightforward - no need to shift values
# Cons
## Extra memory is required - for pointer reference to next memory (and possibly previous) location
## Traversal and reverse traversal - takes longer than indexed access
# Use Cases
## Stack and Queue implementation - CS
## Next and Previous page - Real-world
## 


class singlyLinkedListNode:
    def __init__(self, value, nextNode=None): # we need to ensure the Node doesn't point to anything without explicit instruction to
        self.value = value
        self.nextNode = nextNode
        #self.previousNode = previousNode for doubly linked list

class singlyLinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        newNode = singlyLinkedListNode(value)
        if self.head is None:
            self.head = newNode
            return
            
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = newNode
                return
            currentNode = currentNode.nextNode
            
            
    def insert(self, value, index):
        newNode = singlyLinkedListNode(value)
        counter = 0
        currentNode = self.head
        
        if index == 0:
            newNode.nextNode = self.head
            self.head = newNode
            return
        
        while currentNode is not None:
            if self.head is None:
                self.head = newNode
                return
            if counter == index-1:
                newNode.nextNode = currentNode.nextNode
                currentNode.nextNode = newNode
                return
            if currentNode.nextNode is None:
                if counter != index:
                    print("Index does not exist in list. Appending node at end.")
                currentNode.nextNode = newNode
                return
            currentNode = currentNode.nextNode
            counter += 1
        
        
            
    def get(self, index: int) -> int:
        currentNode = self.head
        counter = 0
        while counter <= index:
            if currentNode is None:
                print("Node " + str(index) + " was not found!")
                break
            if counter == index:
                return currentNode.value
            currentNode = currentNode.nextNode
            counter += 1
    
    
    def print(self) -> str:
        if self.head is None:
            print("List is empty!")
        else:
            currentNode = self.head
            listString = ""
            while currentNode is not None:
                listString += str(currentNode.value)
                if currentNode.nextNode is not None:
                    listString += " -> "
                currentNode = currentNode.nextNode
        print(listString)
    
    
    def delete(self, index):
        if self.head is None:
            print("List is empty, nothing to delete!")
        if index == 0:
            self.head = self.head.nextNode
        else:
            currentNode = self.head
            counter = 0
            while counter <= index:
                if currentNode is None:
                    print("Node " + str(index) + " was not found!")
                    break
                if counter == index-1:
                    currentNode.nextNode = currentNode.nextNode.nextNode
                    break
                currentNode = currentNode.nextNode
                counter += 1
                
        
                
        

#test_list = singlyLinkedList(singlyLinkedListNode(2))
#test_list.append(4)
#test_list.append(3)
#test_list.print()
#test_list.insert(11, 4)
# print(test_list.get(1))
#test_list.print()
#test_list.delete(2)
#test_list.print()
