class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        newNode = Node(value)
        
        if self.size == 0:
            self.top = newNode
            self.size = 1
            return

        newNode.nextNode = self.top
        self.top = newNode
        self.size += 1
        
    def pop(self) -> any:
        
        if self.size == 0:
            return -1 
        
        returnNode = self.top
        self.top = self.top.nextNode
        self.size = self.size - 1
        
        return returnNode.value
    
    def peek(self) -> any:

        if self.size == 0:
            return -1

        return self.top.value
    
class Solution:
    def isValid1(self, s: str) -> bool: # wrote myself 
        
        if len(s) == 0 or len(s) == 1:
            return False
        
        validCharacters = ['(',')','[',']','{','}']
        validStack = Stack()
        
        for element in s:
            if element not in validCharacters:
                return False
            if validStack.size == 0:
                validStack.push(element)
            else:
                stackTop = validStack.peek()
                if stackTop == '(' and element == ')':
                    validStack.pop()
                elif stackTop == '[' and element == ']':
                    validStack.pop()
                elif stackTop == '{' and element == '}':
                    validStack.pop()
                else:
                    validStack.push(element)
                
        return validStack.size == 0
    
    def isValid2(self, s: str) -> bool: # solution from online
        hashmap = {")": "(", "]": "[", "}": "{"}
        validStack = []

        for sign in s:
            if sign not in hashmap: # if sign is not a closing parentheses, append to stack array
                validStack.append(sign)
                continue ## continue to next iteration of loop
            if not validStack or validStack[-1] != hashmap[sign]: # if sign is a closing parentheses (in hashmap), but the stack is empty 
                return False  # OR the top of the stack isn't equivalent to the hash map's open parentheses, 
            validStack.pop() # if sign not a closing parentheses, the stack isn't empty, or if the sign at the top of the 

        return not validStack
        

if __name__ == "__main__":
    
    test_string1 = '([)]'
    test_string2 = "{[]}"
    test_string3 = "()[]{}"
    test_string4 = "()"
    test_string5 = "()x)"
    test_stack = Stack()
        
print(str(Solution().isValid2(test_string5)))