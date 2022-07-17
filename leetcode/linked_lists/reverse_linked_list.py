from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__ (self, head = None):
        self.head = head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # my code
        
        currentNode = head
        numberList = []

        while currentNode != None:
            numberList.append(currentNode.val)
            currentNode = currentNode.next

        # reversedList.reverse()
        newHead = ListNode(numberList[-1])
        currentNode = newHead
        for index in range(len(numberList)-2, -1, -1):
            newNode = ListNode(numberList[index])
            if newHead.next == None:
                newHead.next = newNode
            else:
                currentNode.next = newNode
            currentNode = currentNode.next
            
        return newHead
    
    def reverseList2(self, head: ListNode) -> ListNode: # online code
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode()

print(str(Solution().reverseList(a)))