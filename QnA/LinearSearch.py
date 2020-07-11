# linear search algorithm search values in the list and returns if found

def linear_search(data,value):
    for i in range(len(data)):
        # Returning the index of the value
        if data[i]==value:
            return f"{value} is found at {i} index of provided List"
    #     if not found
    return "Value Not Found"

data=[10, 18, 8, 12, 15, 6, 3, 9, 5]
print(linear_search(data,3))
