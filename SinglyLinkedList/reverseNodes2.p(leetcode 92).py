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
    def reverseNodes(self,left,right):
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        for i in range(right-left):
            temp=curr.next
            curr.next=temp.next
            temp.next=prev.next
            prev.next=temp
        self.head=dummy.next

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
sll.reverseNodes(1,4)
sll.printList()
