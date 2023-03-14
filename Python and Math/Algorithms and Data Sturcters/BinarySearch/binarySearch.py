data = [10,15,22,31,44,50,61,88] # data will be sorted

# big(O)=log(n)

# number=50

def binary_search(number,data,start,end):
    if start>end:
        return f"{number} not found in the list"
    middle=(start+end)//2
    if data[middle]==number:
        return f"Number {number} found at index {middle}"
    elif data[middle]<number:
        return binary_search(number,data,middle+1,end)
    else:
        return binary_search(number,data,start,middle-1)


print(binary_search(5,data,0,len(data)-1))