class Solution:
    def reverseWords(self,s):
        words=[]
        word=""
        for ch in s:

            if ch!=" ":
                word+=ch
            else:
                if word!="":
                    words.append(word)
                    word=""
        if word!="":
            words.append(word)
        result=''
        for i in range(len(words)-1,-1,-1):
            result+=words[i]
            if i!=0:
                result+=" "
        return result
obj=Solution()
print(obj.reverseWords('My name is Rajesh'))