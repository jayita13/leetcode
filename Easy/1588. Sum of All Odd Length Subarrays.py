# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0     
        # checking odd length 
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         if len(arr[i:j+1])%2!=0:
        #             s+= sum(arr[i:j+1])     
        
        # automatically taking odd length
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                s+= sum(arr[i:j+1])
                
        return s 

# Runtime: 72 ms
# Memory Usage: 13.9 MB
