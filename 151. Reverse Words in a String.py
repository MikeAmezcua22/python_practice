class Solution:
  def reverseVowelsString(self, s) -> str:
    s = s.split()
    s.reverse()
    
    return " ".join(s)



s = "  hello world  "
solution = Solution()
print(solution.reverseVowelsString(s))