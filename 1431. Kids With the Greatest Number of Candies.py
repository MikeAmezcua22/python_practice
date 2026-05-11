from typing import List


class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    result = []

    maxCandie = max(candies)

    for i in range(len(candies)):
      result.append(candies[1] + extraCandies >= maxCandie)
    return result
    

candies = [2, 3, 5, 1, 4]
extraCandies = 3

solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))