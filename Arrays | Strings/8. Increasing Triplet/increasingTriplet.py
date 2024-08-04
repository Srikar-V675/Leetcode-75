from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    smallest = middle = float('inf')
    
    for num in nums:
        if num <= smallest:
            smallest = num
        elif num <= middle:
            middle = num
        else:
            return True
    
    return False
