"""
## Number of Good Pairs

### Problem Statement
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
class Solution(object):

    def __init__(self):
        self.count = 0
    
    """
        Below is the brute force approach with O(n^2) time complexity
        only effective for small inputs
    """
    def count_good_pairs(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                 self.count += 1
        return self.count

    """
    Psedou code of an improvement of the solution for running in nlogn time
    if the list has one element then 
        THERE ARE NO PAIRS IN THE lIST
    Else
        Divide the list into two halves:
            A contatins the first half [n/2] elements
            B contains the remaining [n/2] elements
        (gA, A) = disperse(A)     where g is the count of good pairs
        (gB, B) = disperse(B)
        (g, L) = collect_while_counting(A, B)
    Endif
        return gA + gB + g and new L
    
    """    
    def collect_while_counting(self, A, B):      
            i = 0
            j = 0
            merged_list = []
            
            while i < len(A) and j < len(B):
                if A[i] == B[j]:
                    self.count += 1
                    merged_list.append(A[i])
                    merged_list.append(B[j])
                    i += 1
                    j += 1
                elif A[i] < B[j]:
                    i += 1
                else:
                    j += 1
            
            while i < len(A):
                merged_list.append(A[i])
                i += 1
            
            while j < len(B):
                merged_list.append(B[j])
                j += 1
            
            return merged_list
   
    def disperse(self, L):
        if len(L) <= 1:
            return 0, L
        else:
            middle = len(L) // 2
            A = L[:middle]
            B = L[middle:]
            gA, A = self.disperse(A)
            gB, B = self.disperse(B)
            g = self.collect_while_counting(A, B)
        return gA + gB + self.count, g


    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.count = 0
        # this method utilises both the brute force and the divide and conquer approach
        # if the list is less than or equal to 50, the brute force approach is used for showing better performance
        # when the list grows beyond 50, the divide and conquer approach is used.
        return self.count_good_pairs(nums) if len(nums) <= 50 else self.disperse(nums)[0]




# Test case1
sol = Solution()
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums)) # Expected output: 4

# Test case2
sol = Solution()
nums = [1,1,1,1]
print(sol.numIdenticalPairs(nums)) # Expected output: 6

# Test case3
sol = Solution()
print(sol.disperse(nums)[0])

# Test case4
sol = Solution()
nums = [1,2,3,6,3,5,2,3,1,4,2,3,2,2,5,6,7,5,4,2,1,4,6,7,6,8,6,1,1,3,2,4,1,1,1,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
print(sol.numIdenticalPairs(nums)) # Expected output: 10