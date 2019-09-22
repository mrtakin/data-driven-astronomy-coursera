# Write your crossmatch function here.
import numpy as np
import time 
from astropy.coordinates import SkyCoord
from astropy import units as u

def angular_dist(ra1, dec1, ra2, dec2):
  a = np.sin(np.abs(dec1 - dec2) / 2) ** 2
  b = np.cos(dec1) * np.cos(dec2) * (np.sin(np.abs(ra1 - ra2) / 2)) ** 2
                                     
  d = 2 * np.arcsin(np.sqrt(a + b))
  
  return d

def crossmatch(cat1, cat2, max_radius):  
  start = time.perf_counter()
    
  sky_cat1 = SkyCoord(cat1 * u.degree, frame='icrs')
  sky_cat2 = SkyCoord(cat2 * u.degree, frame='icrs')
  closest_ids, closest_dists, _ = sky_cat1.match_to_catalog_sky(sky_cat2)
  
  #print(closest_ids)
  #print(closest_dists)
  #print(np.column_stack((closest_ids, closest_dists.value)))
  
  matches, no_matches = [], []
  for id1, (closest_id, dist) in enumerate(np.column_stack((closest_ids, closest_dists.value))):
    if(dist < max_radius):
      matches.append((id1, closest_id, dist))
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

