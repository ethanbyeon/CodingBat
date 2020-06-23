
def make_chocolate(small, big, goal):
  
  if goal >= 5 * big:
    left = goal - 5 * big
  else:
    left = goal % 5
  
  if left <= small: return left
  return -1
