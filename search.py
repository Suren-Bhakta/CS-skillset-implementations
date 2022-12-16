import sys
import time


def sum_series (v, k):
  # continues to divide the numbers and add to the sum until the sum lines left is zero
  sum = 0
  pow = 0
  lines_left = v
  while lines_left > 0:
  # summing the series
    lines_left = v // (k ** pow)
    sum += lines_left
    pow += 1
  return sum



def linear_search (n, k):
  # Goes through each line needed to write and deduces down to the minimum to be written
  for i in range(n+1):
    if sum_series(i, k) >= n:
      return i
  return i






def binary_search (n, k):
  low = 0
  mid=0
  high = n
  sum=0
  for i in range(n+1):
    if sum_series(i, k) >= n:
      break
    sum = i
  sum+=1
  while(low<=high):
    mid=(low+high)//2
    if mid < sum :
      low = mid+1
    elif mid > sum:
      high=mid-1
    else:
      return mid
  return 0









def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
