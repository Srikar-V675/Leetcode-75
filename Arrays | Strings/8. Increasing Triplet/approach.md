# 1. Problem Definition

**Difficulty:** `Medium`

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

Example 2:

```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

Example 3:

```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

# 2. Approach
To find the triplet (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k], we can use a greedy approach:

1. **Initialization:**

   - Set smallest and middle to a very large value (infinity).
2. Iteration:

   - Iterate through each number in the array nums.
    - If the current number is smaller than smallest, update    smallest.
    - If the current number is not smaller than smallest but -  smaller than middle, update middle.
   - If we find a number larger than middle, we have found our triplet and can return true.

3. Conclusion:

   - If the loop completes without finding such a triplet, return false.
  
This approach ensures that we are always looking for the smallest possible numbers in order.


# 3. Pseudo Code

```
smallest = middle = INF

FOR num in nums
    IF num <= smallest then
        smallest = num
    ELSE IF num <= middle then
        middle = num
    ELSE
        return TRUE

return FALSE
```

# 4. Code

**Time Complexity:** O(N)

**Space Complexity:** O(1)

[[increasingTriplet.py | Python Code]]