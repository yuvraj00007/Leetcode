class Solution:
    def toHex(self, num: int) -> str:
        hm={
            10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"
        }
        if num == 0:
            return "0"
        num &= 0xffffffff
        hex=""
        temp=num
        while temp:
            r=temp%16
            if r>9:
                hex+=hm[r]
            else:
                hex+=str(r)
            temp//=16
        return hex[::-1]
