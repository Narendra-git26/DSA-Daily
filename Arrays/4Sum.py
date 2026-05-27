Time = Big O of n logn + N^3 = O(n^3)

space = O(1) constant space and result (res) O(n) auxiliary space

it was easy if you solve 3 sum as we add just another for loop for 2nd value and two pointer approach for last two values combining (i,j,l,r), we definitely need to sort this array as we are dealing with duplicates and also two pointer approach.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
            
                l , r = j + 1, n - 1
                
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r] 

                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res
