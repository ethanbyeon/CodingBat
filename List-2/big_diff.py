
def big_diff(nums):
  
  mini = maxi = nums[0]
  
  for i in range(1, len(nums)):
    mini = min(mini, nums[i])
    maxi = max(maxi, nums[i])
    
  return maxi - mini
