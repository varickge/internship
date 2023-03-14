data=[3,5,2,7,6,8,1,4]

def qs_easy(data): # big(O)=n*log(n)
    if len(data)<2:
        return data
    pivot=data.pop()
    larger,smaller=[],[]
    for item in data:
        if item>pivot:
            larger.append(item)
        else:
            smaller.append(item)
    return qs_easy(smaller)+[pivot]+qs_easy(larger)

def get_pivot(data,left,right):

    middle=(left+right)//2

    if (data[left]<=data[middle] and data[middle]<=data[right]) or (data[middle]>=data[right] and data[middle]<=data[left]):
        pivotIndex=middle
    elif (data[left]>=data[middle] and data[left]<=data[right]) or (data[left]<=data[middle] and data[right]<=data[left]):
        pivotIndex=left
    elif (data[right]<=data[middle] and data[left]<=data[right]) or (data[middle]<=data[right] and data[right]<=data[left]):
        pivotIndex=right
    return pivotIndex

def sort(data,left,right):
    pivotIndex=get_pivot(data,left,right)
    pivotValue=data[pivotIndex]

    data[pivotIndex],data[left]=data[left],data[pivotIndex]
    border=left
    for i in range(left,right+1):
        if data[i]<pivotValue:
            border+=1
            data[border],data[i]=data[i],data[border]

    data[border],data[left]=data[left],data[border]
    return border

def qs_inplace(data,left,right):
    if left<right:
        border=sort(data,left,right)
        qs_inplace(data,left,border-1)
        qs_inplace(data,border+1,right)

def quick_sort(data):
    qs_inplace(data, 0, len(data)-1)

quick_sort(data)
print(data)