class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_cnt= 0
        max_cnt=0 

        for num in nums:
            if num ==1:
                current_cnt +=1
                max_cnt= max(current_cnt, max_cnt)
            else:
                current_cnt=0
        return max_cnt
