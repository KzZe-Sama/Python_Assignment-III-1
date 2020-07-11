def mergeSort(data):
    if len(data)> 1:
        # dividng into two list
        mid=len(data)//2
        L=data[:mid]
        R=data[mid:]
        mergeSort(L)
        mergeSort(R)

        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                data[k]=L[i]
                i+=1
            else:
                data[k]=R[j]
                j+=1
            k+=1

        while i < len(L):
            data[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            data[k]=R[j]
            j+=1
            k+=1
data=[10, 18, 8, 12, 15, 6, 3, 9, 5]
print("Before Sorting:")
print(data)
print("After Sorting")
mergeSort(data)
print(data)
