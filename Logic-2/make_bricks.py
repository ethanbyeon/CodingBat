
def make_bricks(small, big, goal):
  
  if goal >= 5 * big:
    left = goal - (5 * big)
  else:
    left = goal % 5
    
  return small >= left
