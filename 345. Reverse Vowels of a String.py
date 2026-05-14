class Solution:
  def reverseVowelsStrig(self, s: str) -> str:
    strList = list(s)
    left = 0
    right = len(strList) -1

    vowels = "aeiouAEIOU"
    while left < right:
     
     if strList[left] not in vowels:
       left += 1
     elif strList[right] not in vowels:
       right -= 1
     else:
       strList[left], strList[right] = strList[right], strList[left]
       left += 1
       right -= 1


    return "".join(strList)


s = "IceCreAm"
solution = Solution()
print(solution.reverseVowelsStrig(s))