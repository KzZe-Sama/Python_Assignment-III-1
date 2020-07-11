def quick_sort(data,low,high):

    if low < high:
        pivot=partition(data,low,high)
        quick_sort(data,low,pivot-1)
        quick_sort(data,pivot+1,high)

    return data

# Getting pivot element
def pivot(data,low,high):
    mid=(low+high)//2
    pivot=high
    if data[low] < data[mid]:
        if data[high]>data[mid]:
            pivot=mid
    elif data[low] < data[high]:
        pivot=low
    return pivot
def partition(data,low,high):
    pivotIndex=pivot(data,low,high)
    pivotValue=data[pivotIndex]
    data[pivotIndex],data[low]=data[low],data[pivotIndex]
    border=low

    for i in range(low,high+1):
        if data[i]< pivotValue:
            border=border+1
            data[i],data[border]=data[border],data[i]
    data[low],data[border]=data[border],data[low]
    return border
if __name__=="__main__":
    data=[10, 18, 8, 12, 15, 6, 3, 9, 5]
    low=0
    high=len(data)-1
    print("Before Sort:")
    print(data)
    print("After Sort:")
    print(quick_sort(data,low,high))