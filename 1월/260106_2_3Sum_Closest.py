from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best_s = 100000
        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            while left < right:
                sumNum = nums[i] + nums[left] + nums[right]

                if target == sumNum:
                    return sumNum
                
                if abs(target - sumNum) < abs(target - best_s):
                    best_s = sumNum
                
                if sumNum <= target:
                    left += 1
                else:
                    right -= 1
            
        return best_s

test = Solution()
# print(test.threeSumClosest([-1,2,1,-4], 1))
# print(test.threeSumClosest([0,1,2], 3))
# print(test.threeSumClosest([10,20,30,40,50,60,70,80,90], 1))
print(test.threeSumClosest([-1000,-1000,-1000], 10000))