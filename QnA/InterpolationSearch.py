# This Algorithm only works on sorted List
def Interpolation_seatch(data,value):
    # Initialzing the Start and end point of the list for loop
    start=0
    end=len(data)-1
    # Loop runs if start value is small or equal to end value and the
    # value we are searching is greater then or equal to start value and less then or equal to end value
    while start<=end and value>=data[start] and value<=data[end]:
        # this is the formula to current position
        pos=start+((end-start)/(data[end]-data[start]))*(value-data[start])
        pos=int(pos)
        # if value is found at that position
        if data[pos]==value:
            return f"{value} was found at {pos} index"
        # if the positional value is less than value we are searching we increase start point
        elif value>data[pos]:
            start=pos+1
        # if the positional value is more than value we are searching we decrease stop point
        else:
            end=pos-1
    return f"{value} was not found"

data=[10, 18, 8, 12, 15, 6, 3, 9, 5]
print("Sorting List if not sorted:")

data=sorted(data)
print("Sorted  New List ")
print(data)
# Only Works on sorted List
print(Interpolation_seatch(data,5))