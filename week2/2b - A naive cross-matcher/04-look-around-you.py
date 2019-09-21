# Write your find_closest function here
import numpy as np

def hms2dec(h, m, s):
  return 15 * dms2dec(h, m, s)

def dms2dec(h, m, s):
  return (abs(h) + m / 60 + s / (60*60)) * (-1 if h < 0 else 1)

def angular_dist(ra1, dec1, ra2, dec2):
  ra1 = np.radians(ra1)
  dec1 = np.radians(dec1)
  ra2 = np.radians(ra2)
  dec2 = np.radians(dec2)
  
  a = np.sin(np.abs(dec1 - dec2) / 2) ** 2
  b = np.cos(dec1) * np.cos(dec2) * (np.sin(np.abs(ra1 - ra2) / 2)) ** 2
                                     
  d = 2 * np.arcsin(np.sqrt(a + b))
  
  return np.degrees(d)

def import_bss():
  cat = np.loadtxt('bss.dat', usecols = range(1, 7))
  
  return list(map(lambda i: (i+1, hms2dec(*cat[i][0:3]), 
                                  dms2dec(*cat[i][3:6])), range(len(cat))))

def find_closest(cat, ra, des):
  # map (id, coordinates) list to (id, dist) list
  cat_dists = map(lambda cat_item: (cat_item[0], angular_dist(cat_item[1], cat_item[2], ra, des)), cat)
  
  # find the closest object's (id, dist) from given
  closest_cat_item = min(cat_dists, key=lambda cat_dist: cat_dist[1])
                 
  return closest_cat_item


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))

