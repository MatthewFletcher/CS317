def mergeSort(arr,s=""): 
    _ = input("cont?")
    if len(arr) >1: 
        mid = len(arr)//2 #Using integer division
        L = arr[0:mid] # Dividing the array elements  
        R = arr[mid:len(arr)] # into 2 halves 
  
        #Recursively sort the arrays
        if(s=='r'):
            print("Sorting Right Side")
        print("Array value in this recursion: ", arr)
        mergeSort(R, 'r')
        print()

        if(s=='l'):
            print("Sorting Left Side")
        print("Array value in this recursion: ", arr)
        mergeSort(L, 'l')
        print()
  
        i = 0
        j = 0
        k = 0
          
        #Copy the first half of the array in L to the first half 
        #of the main array, and the second half of the array in R
        # to the second half of the main array.  
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        #If any elements are left, fill them in automagically
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
def main():
    arr = [1,5,3,9,7,12,15,45,96]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

if __name__ == '__main__':
    main()