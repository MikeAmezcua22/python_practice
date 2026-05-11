from typing import List

class Solution:
  def canPlaceFlower(self, flowerBed: List[int], n: int) ->  List:
    planted=0
    flowerBedCopy = flowerBed.copy()

    for i in range(len(flowerBedCopy)):
      if flowerBedCopy[i] == 0:
        empy_left = (i == 0) or (flowerBedCopy[i  + 1] == 0)
        empty_right = (i == len(flowerBed) -1) or (flowerBedCopy[i -1] == 0)

        if empty_right and empy_left:
          planted += 1
          flowerBed[i] = 1

    return planted >= n

plot = [1, 0, 0, 0, 1]
n = 2

solution = Solution()
print(solution.canPlaceFlower(plot, n))