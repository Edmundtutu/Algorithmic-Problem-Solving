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
    def numIdenticalPairs(self):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Below is the brute force approach with O(n^2) time complexity 
        # only effective for small inputs
        count = 0
        nums = self.nums
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                 count += 1
        return count
    