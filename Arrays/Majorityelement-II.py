# LeetCode 229 - Majority Element II
# Topic: Arrays
# Difficulty: Medium

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # base case 
        if not nums:
            return []

        # each count to calculate its latest frequency whether it is dominating or not and cands for two values as for n//3 we cant have more than two majority elements with mathematical logic if n = 9 we need atleast 4 or greater than (>) 3 to be an majority element.

        # if [1,1,1,2,2,2,2,3,3] in this only 2 is qualified as majority element

        count1, count2 = 0,0
        cand1 = None
        cand2 = None

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        result = []

        #reset counter too zeroes again to count their frequencies
        count1, count2 = 0,0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        if count1 > n//3:
            result.append(cand1)
        if count2 > n//3:
            result.append(cand2)
        
        return result
