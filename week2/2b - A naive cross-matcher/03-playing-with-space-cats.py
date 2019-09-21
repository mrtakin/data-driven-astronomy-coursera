# Write your import_bss function here.
import numpy as np

def hms2dec(h, m, s):
  return 15 * dms2dec(h, m, s)
    
def dms2dec(h, m, s):
  return (abs(h) + m / 60 + s / (60*60)) * (-1 if h < 0 else 1)

def import_bss():
  cat = np.loadtxt('bss.dat', usecols = range(1, 7))
  
  return list(map(lambda i: (i+1, hms2dec(*cat[i][0:3]), 
                                  dms2dec(*cat[i][3:6])), range(len(cat))))

def import_super():    
  cat = np.loadtxt('super.csv', delimiter = ',', skiprows = 1, usecols = [0, 1])
  
  return list(map(lambda i: (i+1, cat[i][0], cat[i][1]), range(len(cat))))
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
