def reverse(arr, left, right):   
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1 
  return arr
def solution(arr, k):
    if len(arr) > 0:
      n = len(arr)
      reverse(arr, 0, n-1)
      reverse(arr, 0, k%n-1)
      reverse(arr, k%n,n-1)
    return arr
