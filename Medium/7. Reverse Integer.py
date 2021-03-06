# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        s=0
        n = abs(x)
        while n>0:            
            s=s*10+n%10
            n//=10
        if s.bit_length() < 32:
            if x<0:
                return -1*s
            else:
                return s
        else:
            return 0
    
# Runtime: 32 ms
# Memory Usage: 13.9 MB        
