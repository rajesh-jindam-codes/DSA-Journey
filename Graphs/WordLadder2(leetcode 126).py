from collections import defaultdict, deque
class Solution:
    def findLadders(self,beginWord,endWord,wordList):
        wordSet=set(wordList)
        if endWord not in wordSet:
            return []
        parents=defaultdict(list)
        queue=deque([beginWord])
        visited=set([beginWord])
        found=False
        while queue and not found:
            localVisited=set()
            for _ in range(len(queue)):
                word=queue.popleft()
                wordChars=list(word)
                for i in range(len(wordChars)):
                    original=wordChars[i]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch==original:
                            continue
                        wordChars[i]=ch
                        newWord="".join(wordChars)
                        if newWord in wordSet:
                            if newWord not in visited:
                                if newWord not in localVisited:
                                    queue.append(newWord)
                                    localVisited.add(newWord)
                                parents[newWord].append(word)
                        if newWord==endWord:
                            found =True
                    wordChars[i]=original
            visited.update(localVisited)
        result=[]
        def dfs(word,path):
            if word==beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                dfs(parent,path+[parent])
        if found:
            dfs(endWord,[endWord])
        return result
beginWord='hit'
endWord='cog'
wordList=["hot","dot","dog","lot","log","cog"]
obj=Solution()
print(obj.findLadders(beginWord,endWord,wordList))