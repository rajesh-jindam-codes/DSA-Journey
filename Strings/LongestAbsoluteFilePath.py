class Solution:
    def longestAbsoluteFilePath(self,input):
        maxLen=0
        pathLen={0:0}
        for line in input.split("\n"):
            depth=line.count('\t')
            name=line.strip('\t')
            nameLen=len(name)

            if "." in name:
                maxLen=max(maxLen,pathLen[depth]+nameLen)
            else:
                pathLen[depth+1]=pathLen[depth]+nameLen+1
        return maxLen
obj=Solution()
input = input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(obj.longestAbsoluteFilePath(input))