
def sum67(nums):
  
  total = 0
  six = False
  
  for i in range(len(nums)):
    if nums[i] == 6: six = True
    if not six: total += nums[i]
    if nums[i] == 7 and six: six = False
    
  return total

