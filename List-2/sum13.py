
def sum13(nums):
  
  sum = i = 0
  
  while i < len(nums):
    if nums[i] == 13: i += 1
    else: sum += nums[i]
    
    i += 1
    
  return sum
