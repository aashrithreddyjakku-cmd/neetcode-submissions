class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for x in strs:
            encoded.append(str(len(x))+"#"+x)
            
        return "".join(encoded)



        

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i < len(s):
            j=s.find("#",i)
            length=int(s[i:j])

            word=s[j+1:j+length+1]

            res.append(word)

            i = j+1+length
        return res




