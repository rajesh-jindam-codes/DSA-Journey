class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if len(self.items)==0:
            return 'queue is empty'
        x=self.items.pop(0)
        return x
    def size(self):
        return len(self.items)
    def front(self):
        if len(self.items)==0:
            return 'queue is empty'
        return self.items[0]
    def rear(self):
        if len(self.items)==0:
            return 'queue is empty'
        return self.items[-1]
queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.items)
print(queue.dequeue())