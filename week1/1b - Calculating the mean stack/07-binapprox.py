import numpy as np

# Write your median_bins and median_approx functions here.
def median_bins(data, B):
  data_array = np.asarray(data) # Convert it to np array
  
  mean = np.mean(data_array)
  std = np.std(data_array)
  
  min_val, max_val = (mean - std), (mean + std)
  bin_width = 2 * std / B
  
  bin_counts = np.zeros(B+1)
  bin_counts[0] = len(data_array[data_array < min_val]) # Ignore values lower than min_val
    
  for i in range(1, B+1):
    bin_counts[i] = len(data_array[data_array < min_val + i * bin_width]) - sum(bin_counts[:i])

  return (mean, std, int(bin_counts[0]), bin_counts[1:])

def median_approx(data, B):
  mean, std, ignore_counts, bin_counts = median_bins(data, B)
  bin_width = 2 * std / B
  min_value = mean - std
                                                     
  until = (len(data) + 1) / 2
  
  count = ignore_counts
  for bin_number, x in enumerate(bin_counts):
    count += x
    if count >= until:
      break
      
  return min_value + bin_number * bin_width + 0.5*bin_width
  

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))

