def quicksort(arr, left, right):
  if(left < right):
    print(arr)
    pivot = partition(arr, left, right)
    print("^^Pivot = {}^^".format(arr[pivot]))
    print()
    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)
  return arr

def partition(arr, left, right):
  pivot = left
  left += 1
  while True:
    #While l<=r and l hasn't reached pivot yet
    while left <= right and arr[left] < arr[pivot]:
        #Shift left to the right
      left += 1
    #While l<r and r hasn't reached pivot 
    while left <= right and arr[right] > arr[pivot]:
        #Shift right to the left
      right -= 1

    #If left and right did not cross, swap them and continue
    if left <= right:
      swap(arr, left, right)
      left += 1
      right -=1
    #Otherwise, break
    if left > right:
      break
  #Swap algorithm 
  swap(arr, right, pivot)
  return right

def swap(arr, a, b):
    c = arr[a]
    arr[a] = arr[b]
    arr[b] = c


def main():
    # Driver code to test above 
    arr = [9,8,7,6,5,4,3,2,1] 
    print("Original list: ")
    print(arr, sep=",")
    print()
    n = len(arr) 
    print("Implementing quicksort:")
    quicksort(arr,0,n-1) 
    print(arr,sep=",") 
    
if __name__ == '__main__':
    main()