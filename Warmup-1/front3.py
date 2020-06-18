
def front3(str):
  front = ''
  if len(str) >= 3: front = str[:3]
  elif len(str) < 3: front = str
  return (3 * front)
  