
def count_hi(str):
  
  total = 0
  
  for i in range(len(str) - 1):
    if str[i: i + 2] == 'hi':
      total += 1
      
  return total
