class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#initialize a hashset
        hashset = set()
        #traverse through array
        for i in nums:
            #check if element is already present in hashset
            if i in hashset:
                #return true if element does exist
                return True
            #add element to hashset if it does not exist
            hashset.add(i)
        #return false if no duplicate elements are found
        return False