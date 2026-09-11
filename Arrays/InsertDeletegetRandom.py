import random
class RandomSet(object):
    def __init__(self):
        self.nums=[]
        self.index={}
    def insert(self,val):
        if val in self.index:
            return False
        self.index[val]=len(self.nums)
        self.nums.append(val)
        return True
    def remove(self,val):
        if val not in self.index:
            return False
        index=self.index[val]
        last=self.nums[-1]
        self.nums[index]=last
        self.nums.pop()
        del self.index[val]
        return True
    def getRandom(self):
        return random.choice(self.nums)
obj = RandomSet()

print(obj.insert(1))      # True
print(obj.remove(2))      # False
print(obj.insert(2))      # True
print(obj.getRandom())    # 1 or 2
print(obj.remove(1))      # True
print(obj.insert(2))      # False
print(obj.getRandom())    # 2