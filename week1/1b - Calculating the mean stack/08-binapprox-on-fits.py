# Import the running_stats function
from helper import running_stats
from astropy.io import fits
import numpy as np
# Write your median_bins_fits and median_approx_fits here:

def median_bins_fits(files, bin_number):
  mean, std = running_stats(files)
  
  x, y = mean.shape
  
  min_val, max_val = (mean - std), (mean + std)
  bin_width = 2 * std / bin_number
  
  bin_counts = np.zeros([x, y, bin_number+1])
  bin_ignores = np.zeros([x, y])
  
  for file in files:
    data = fits.open(file)[0].data
    
    bin_ignores += 1 * (data < min_val)
    
    for i in range(1, bin_number+1):
      bin_counts[:,:,i] += 1 * ((data < (min_val + i * bin_width)) & (data > min_val + (i - 1) * bin_width))
  
  return mean, std, bin_ignores, bin_counts[:, :, 1:]

def median_approx_fits(files, bin_number):
  mean, std, bin_ignores, bin_counts = median_bins_fits(files, bin_number)
  bin_width = 2 * std / bin_number
  min_value = mean - std
  
  until = (len(files) + 1) / 2
  
  x, y = mean.shape
  median = np.zeros([x, y])
  for i in range(x):
    for j in range(y):
        count = bin_ignores[i, j]
        for bin_number, value in enumerate(bin_counts[i, j, :]):
          count += value
          if count >= until:
            break
            
        median[i, j] = min_value[i, j] + bin_number * bin_width[i, j] + 0.5 * bin_width[i, j]
          
  return median          

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  print(bins[100, 100, :])
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  print(median[100, 100])
  
  mean, std, left_bin, bins = median_bins_fits(['image{}.fits'.format(str(i)) for i in range(11)], 4)
  print(bins[100, 100, :])
  median = median_approx_fits(['image{}.fits'.format(str(i)) for i in range(11)], 4)
  print(median[100, 100])
  
