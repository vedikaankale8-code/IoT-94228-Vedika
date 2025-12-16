def overlapping_loops(list1, list2):
  for item1 in list1:
    for item2 in list2:
      if item1 == item2:
        return True  
  return False 

            