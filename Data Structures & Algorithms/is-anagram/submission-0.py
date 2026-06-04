class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in t:
            if i in freq:
                freq[i]-=1
            else:
                freq[i]=1
        for i,count in freq.items():
            if count != 0:
                return False
        return True
        