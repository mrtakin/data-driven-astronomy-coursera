# Write your hms2dec and dms2dec functions here
def hms2dec(h, m, s):
  return 15 * dms2dec(h, m, s)
    
def dms2dec(h, m, s):
  return (abs(h) + m / 60 + s / (60*60)) * (-1 if h < 0 else 1)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))Convert to decimal degrees
