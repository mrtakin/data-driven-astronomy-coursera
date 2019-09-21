# Write your crossmatch function here.
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

def import_super():    
  cat = np.loadtxt('super.csv', delimiter = ',', skiprows = 1, usecols = [0, 1])
  
  return list(map(lambda i: (i+1, cat[i][0], cat[i][1]), range(len(cat))))

def angular_dist(ra1, dec1, ra2, dec2):
  ra1 = np.radians(ra1)
  dec1 = np.radians(dec1)
  ra2 = np.radians(ra2)
  dec2 = np.radians(dec2)
  
  a = np.sin(np.abs(dec1 - dec2) / 2) ** 2
  b = np.cos(dec1) * np.cos(dec2) * (np.sin(np.abs(ra1 - ra2) / 2)) ** 2
                                     
  d = 2 * np.arcsin(np.sqrt(a + b))
  
  return np.degrees(d)

def crossmatch(bss_cat, super_cat, max_dist):
  matches, no_matches = [], []
  for bss_id, bss_ra, bss_dec in bss_cat:
    min_dist = np.inf
    min_dist_id = -1
    
    for super_id, super_ra, super_dec in super_cat:
      dist = angular_dist(bss_ra, bss_dec, super_ra, super_dec)
      
      if dist < min_dist:
        min_dist = dist
        min_dist_id = super_id
    
    if(min_dist < max_dist):
      matches.append((bss_id, min_dist_id, min_dist))
    else:
      no_matches.append(bss_id)
      
  return matches, no_matches    

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

