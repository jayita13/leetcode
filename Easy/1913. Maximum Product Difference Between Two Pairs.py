# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

def maxProductDifference(self, nums: List[int]) -> int:
        n = sorted(nums)
        return n[-1]*n[-2] - n[0]*n[1]

# Runtime: 172 ms
# Memory Usage: 15.4 MB
