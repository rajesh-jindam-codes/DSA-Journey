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
    def deleteNthNode(self,n):
        temp=self.head
        length=0
        while temp is not None:
            length+=1
            temp=temp.next
        if length==n:
            self.head=self.head.next
            return
        positiontoStop=length-n
        count=1

        temp=self.head
        while count<positiontoStop:
            temp=temp.next
            count+=1
        temp.next=temp.next.next
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
sll.deleteNthNode(1)
sll.printList()