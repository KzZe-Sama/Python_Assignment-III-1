def binary_search(data,x):
    L=0
    R=len(data)-1
    while L<=R:
        m=(L+R)//2
        if data[m]< x:
            L=L+1
        elif data[m]>x:
            R=R-1
        else:
            return f"{x} was found at {m} index"
    return f"{x} was not found"

# Procedure
dataA=[3,2,1,5,4,7,8,11,10]
print(dataA)
print(sorted(dataA))
print(binary_search(sorted(dataA),11))