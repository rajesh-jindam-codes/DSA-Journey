from collections import deque
beginWord='hit'
endWord='cog'
wordList=["hot","dot","dog","lot","log","cog"]
class Solution:
    def ladderLength(self,beginWord,endWord,wordList):
        wordSet=set(wordList)
        if endWord not in wordList:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while queue:
            currWord,level=queue.popleft()
            if currWord==endWord:
                return level
            for i in range(len(currWord)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch==currWord[i]:
                        continue
                    newWord=currWord[:i]+ch+currWord[i+1:]
                    if newWord in wordList:
                        queue.append((newWord,level+1))
                        wordSet.remove(newWord)
        return 0
obj=Solution()
print(obj.ladderLength(beginWord,endWord,wordList))