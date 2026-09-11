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
    def printList(self):
            temp=self.head
            while temp:
                print(temp.val,end="->")
                temp=temp.next
            print('None')
    def reorder(self,head):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        first=self.head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2
sll=singlyLinkedList()
sll.append(2)
sll.append(4)
sll.append(3)
sll.append(40)
sll.append(50)         
sll.printList()
sll.reorder(2)
sll.printList()