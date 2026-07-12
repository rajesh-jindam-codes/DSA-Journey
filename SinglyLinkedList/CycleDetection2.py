class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singlyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    def cycleDetect(self):
        slow=self.head
        fast=self.head
        while fast is None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return "no cycle found"
        slow=self.head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
    def printList(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print('None')
sll=singlyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.printList()
print(sll.cycleDetect())