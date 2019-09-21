# Write your function median_FITS here:
import sys
import time
import numpy as np
from astropy.io import fits

def median_fits(files):
  data_array = np.asarray(
    list(map(lambda file: fits.open(file)[0].data, files)))
  
  start = time.perf_counter() 
  
  median_image = np.median(data_array, axis=0)
  time_to_calc = time.perf_counter() - start
  memory = data_array.nbytes / 1024
  
  return (median_image, time_to_calc, memory)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])
