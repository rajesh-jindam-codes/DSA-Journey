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
    def looplength(self):
        temp=self.head
        travel=0
        myset=dict()
        while temp is not None:
            if temp in myset:
                print(travel-myset(temp))
            myset[temp]=temp
            travel+=1
            temp=temp.next
        print("noe loop Occured")
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
sll.looplength()