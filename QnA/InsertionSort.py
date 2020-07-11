def ins_sort(Data):
    # Iteration from 1 index of the List
    for i in range(1,len(Data)):
        value=Data[i]
        j=i-1
        # running while loop only if j is greater or equals to 0 and
        # comparing two indexes from list and swapping them if back one is
        # greatert than the first one
        while j>=0 and value < Data[j]:
            Data[j+1]=Data[j]
            j-=1
        Data[j+1]=value

    return Data

print(ins_sort([14,33,27,10,35,19,42,44]))
