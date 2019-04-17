#!/usr/bin/env python3
#LAZY MAN'S QUICK SORT


#Manual quicksort to implement printing of the pivot, left, and right pointers automagically. 
def quicksort(arr, left, right):
  if(left.digit < right.digit):
    printlist(arr)
    pivot = partition(arr, left, right)
    print("^^Pivot = {}^^".format(arr[pivot].digit))
    print()
    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)
  return arr

def partition(arr, left, right):
  pivot = left.digit
  left.dtype='P'
  left += 1
  while True:
    #While l<=r and l hasn't reached pivot yet
    while left.digit <= right.digit and arr[left].digit < arr[pivot]:
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
  return right.digit

def swap(arr, a, b):
    c = arr[a].digit
    arr[a].digit = arr[b].digit
    arr[b].digit = c

def printlist(arr):
    for item in arr:
        print(item.digit, sep="\t")
    for item in arr:
        print(item.dtype, sep='\t')


def main():
    
    class SortStruct():
        def __init__(self, digit, dtype):
            self.digit = digit
            self.dtype = dtype
    arr = [9,8,7,6,5,4,3,2,1]
    list = []
    for i, num in enumerate(arr):
        list.append(SortStruct(num, ''))
        print(list[i].digit, end=' ')

    # Driver code to test above 
    print("Original list: ")
    printlist(list)
    print()
    n = len(list) 
    print("Implementing quicksort:")
    quicksort(list,0,n-1) 
    printlist(list) 
    
if __name__ == '__main__':
    main()
