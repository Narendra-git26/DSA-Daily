Time = O(N^2) + O(Nlogn) = O(N^2)
space = O(N) or O(1) constant space


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []


        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l , r = i + 1, len(nums) - 1

            while l < r:
                csum = nums[i] + nums[l] + nums[r]

                if csum < 0:
                    l += 1
                elif csum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
