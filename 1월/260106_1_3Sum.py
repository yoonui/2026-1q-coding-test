from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            while left < right:
                sumNum = nums[i] + nums[left] + nums[right]
                if sumNum > 0:
                    right -= 1
                elif sumNum < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
        return answer

test = Solution()
# print(test.threeSum([-1,0,1,2,-1,-4]))
# print(test.threeSum([0,0,0]))
print(test.threeSum([-100,-70,-60,110,120,130,160]))