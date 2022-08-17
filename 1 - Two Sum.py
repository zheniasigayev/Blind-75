class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {} # Key = value at index, Value = index of value 
        for index, value in enumerate(nums): # Loops through array
            complement = target - value # Finds complement as that needs to exist for there to be a pair-sum
            if complement in dict: # Will return False on 1st pass since nothing has been added
                return [dict[complement], index] # Returns value (which was set to be index) and current index
            else:
                dict[value] = index # Sets key to value and value to index (e.g., {2, 0})  

    """
    1. Create dictionary which will store {Value , Index} pairs
    2. Loop through nums array
    3. For each iteration, calculate the complement by subtracting value at index from target
    4. Check if complement is in dictionary (False on 1st pass)
        4.1. If True, return the value that's stored at the complement key and current index 
        4.2. If False, create key which is Value at current index, and set it's value to current index   
    
    
    This works because if complement isn't in dict, then we append the current value as a key in the dict. 
    Since there is ALWAYS 1 solution, then eventually there will be a complement that will be equal to a key in the         dict. At this point, you return value (which was index we previously stored) and the current index.
    
    
    Runtime: O(n) - Loops through entire array once
    Memory: O(n) - Potential to add all nums to dictionary
    
    
    """