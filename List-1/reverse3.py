
def reverse3(nums):
  
  temp = nums[-1]
  nums[-1] = nums[0]
  nums[0] = temp
  
  return nums
