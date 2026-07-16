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
sll=singlyLinkedList()
sll.append(10)
sll.append(20)
sll.printList()
