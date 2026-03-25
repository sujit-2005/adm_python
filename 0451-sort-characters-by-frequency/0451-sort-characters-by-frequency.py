class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        freq= sorted(freq.items(), key=lambda item: item[1], reverse=True)
        st=""
        for j, i in freq:
            st+=j*i
        return st