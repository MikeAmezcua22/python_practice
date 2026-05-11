from math import gcd

class Solution:
  def gcdOfString(self, str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
      return ""
    
    result = gcd(len(str1), len(str2))

    return result