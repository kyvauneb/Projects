class Node:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class MinStack:

    def __init__(self):
        self.head = None
        self.size = 0
        self.minValue = None ## for each element in the stack, push the current minimum value

    def push(self, val: int):
        newNode = Node()
        if self.head is None:
            self.minValue = val
            newNode.value = (val, self.minValue)
            self.head = newNode
            self.size += 1
            return
        
        self.minValue = self.head.value[1] # get the current minimum value
        
        if val < self.minValue:
            self.minValue = val
        newNode.value = (val, self.minValue)
        newNode.nextNode = self.head
        self.head = newNode
        self.size += 1

    def pop(self) -> any:
        self.head = self.head.nextNode
        self.size = self.size - 1
        if self.head is None:
            self.minValue = None # if stack is empty, as should be the minValue

    def top(self) -> int:
        return self.head.value[0]

    def getMin(self) -> int:
        return self.head.value[1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-10)
obj.push(14)
obj.getMin()
obj.getMin()
obj.push(-20)
obj.getMin()
obj.getMin()
obj.top()
obj.getMin()
obj.pop()
obj.push(10)
obj.push(-7)
obj.getMin()
obj.push(-7)
obj.pop()
obj.top()
obj.getMin()
obj.pop()



# Output [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
# Expected [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]