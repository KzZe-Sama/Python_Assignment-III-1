# bubble sort algorithm

# the function sorts list of numbers in ascending order
def sortList(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if(j!=len(data)-1):
                if data[j]>data[j+1]:
                # creating temp var and storing before swapping
                    temp=data[j]
                    data[j]=data[j+1]
                    data[j+1]=temp

    return data

# data

dataA=[3,4,6,7,9,1,2,5,8]
dataB=[30,40,60,70,90,10,20,50,80]
print("Unsorted Data:")
print(dataA)
print(dataB)
# Calling FUnction
print("Sorted List using Bubble Sort Algorithm:")
print(sortList(dataA))
print(sortList(dataB))