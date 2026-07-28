from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Stores parent relationships
        parents = defaultdict(list)

        queue = deque([beginWord])

        visited = set([beginWord])

        found = False

        while queue and not found:

            local_visited = set()

            for _ in range(len(queue)):

                word = queue.popleft()

                word_chars = list(word)

                for i in range(len(word_chars)):

                    original = word_chars[i]

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == original:
                            continue

                        word_chars[i] = ch
                        new_word = "".join(word_chars)

                        if new_word in wordSet:

                            # First time in this level
                            if new_word not in visited:

                                if new_word not in local_visited:
                                    queue.append(new_word)
                                    local_visited.add(new_word)

                                parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

                    word_chars[i] = original

            visited.update(local_visited)
        result = []
        # DFS to reconstruct paths
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        if found:
            dfs(endWord, [endWord])

        return result
beginWord='hit'
endWord='cog'
wordList=["hot","dot","dog","lot","log","cog"]
obj=Solution()
print(obj.findLadders(beginWord,endWord,wordList))