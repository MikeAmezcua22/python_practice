class Solution:
  def productOfArray(self, nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [0] * n
    
    left = 1
    for i in range(n):
      answer[i] = left
      left *= nums[i]
      
      print(answer)
    right = 1
    for i in range(n -1, -1, -1):
      answer[i] *= right
      right *= nums[i]
      
      
    return answer
  
  

nums = [1, 2, 3, 4]
solution = Solution()

print(solution.productOfArray(nums))


# [1, 0, 0, 0]
# [1, 1, 0, 0]
# [1, 1, 0, 0]