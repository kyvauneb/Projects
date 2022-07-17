# Python program to demonstrate stack implementation using a linked list.



class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class StackList:

  # Initializing a stack.
  # Use a dummy node, which is easier for handling edge cases.
    def __init__(self):
        self.top = None
        self.size = 0

    # String representation of the stack
    def print(self):
        if self.top is None:
            return "Stack is empty"
    
        stackString = ""
        currentNode = self.top
        counter = 0
    
        while currentNode is not None:
            stackString = "Node " + str(counter) + " is: " + str(currentNode.value)
            print(stackString)
            currentNode = currentNode.nextNode
            counter += 1
        
        return "done"


    # Get the current size of the stack
    def getSize(self) -> int:
        return self.size


    # Check if the stack is empty
    def isEmpty(self) -> bool:
        return self.size == 0


  # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we are peeking an empty stack.
        if self.size == 0:
            print("Nothing to peek - stack is empty!")
            return

        return self.top.value

    # Push a value into the stack.
    def push(self, value):
        newNode = Node(value)

        if self.size == 0:
            self.top = newNode
            self.size = 1
            return

        newNode.nextNode = self.top
        self.top = newNode
        self.size += 1
        


    # Remove a value from the stack and return.
    def pop(self) -> any:
        if self.size == 0:
            print("Nothing to pop - stack is empty")
            return
        
        returnNode = self.top
        self.top = self.top.nextNode
        
        return returnNode.value
    


# Driver Code
if __name__ == "__main__":

    test_stack = StackList()
    for i in range(1, 11):
        test_stack.push(i)
    test_stack.print()

    for _ in range(1, 6):
        remove = test_stack.pop()
        print(f"Pop: {remove}")
    test_stack.print()
