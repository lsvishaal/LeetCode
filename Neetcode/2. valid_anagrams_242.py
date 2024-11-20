class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

# Time complexity: O(nlogn)
# Space complexity: O(1)
# Approach: Sort the strings and compare them. If they are equal, return True else False.