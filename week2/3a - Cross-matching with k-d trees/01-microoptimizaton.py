# Write your crossmatch function here.
import numpy as np
import time 

def angular_dist(ra1, dec1, ra2, dec2):
  a = np.sin(np.abs(dec1 - dec2) / 2) ** 2
  b = np.cos(dec1) * np.cos(dec2) * (np.sin(np.abs(ra1 - ra2) / 2)) ** 2
                                     
  d = 2 * np.arcsin(np.sqrt(a + b))
  
  return d

def crossmatch(cat1, cat2, max_radius):
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  max_radius = np.radians(max_radius)
  
  start = time.perf_counter()
  
  matches, no_matches = [], []
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_dist_id = -1
    
    for id2, (ra2, dec2) in enumerate(cat2):
      dist = angular_dist(ra1, dec1, ra2, dec2)
      
      if dist < min_dist:
        min_dist = dist
        min_dist_id = id2
    
    if(min_dist < max_radius):
      matches.append((id1, min_dist_id, np.degrees(min_dist)))
    else:
      no_matches.append(id1)
      
  return matches, no_matches, (time.perf_counter() - start) 


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

