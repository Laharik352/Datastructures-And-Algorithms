'''Implementation fof Merge sort'''
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        MergeSort(lefthalf)     # Here, we are breaking down the entire array into a single element recursively and
        MergeSort(righthalf)    # simultaneously moving a part of it to the right and the other to the left

        i = 0       # tracker for the left half
        j = 0       # tracker for the right half
        k = 0       # tracker for the final array

        while i<len(lefthalf) and j<len(righthalf):     # When the lenght of the arr is 2, the further division will stop.
                                                        # Then, swapping and creation of the sorted array will start.
            if lefthalf[i] < righthalf[j]:      #compare each element of left half with that of the righthalf and append the smaller element first to the final array
                arr[k] = lefthalf[i]
                i+=1
            else:
                arr[k] = righthalf[j]
                j+=1
            k+=1                                # Increment k so that the next element goes to the next index

        while i<len(lefthalf):          # When all the elements of the right half have got completed in the before while loop
            arr[k]=lefthalf[i]          # Add the elements in the left half to the array
            i+=1
            k+=1

        while j<len(righthalf):         # When all the elements of the left half have got completed in the before before while loop
            arr[k] = righthalf[j]       # Add the elements in the right half to the array
            j+=1                        # The three while loops are doing the merging of the sorted sublists
            k+=1

    # print("Merging",arr)
    return arr

print(MergeSort([11,2,5,4,7,56,2,12,13]))

