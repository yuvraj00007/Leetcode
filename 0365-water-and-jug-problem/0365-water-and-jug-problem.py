class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def gcd(a,b):
            while b:
                temp=b
                b=a%b
                a=temp
            return a
        z=target
        if x+y<z:
            return False
        if x==z or y==z or x+y==z:
            return True
        return z%gcd(x,y)==0