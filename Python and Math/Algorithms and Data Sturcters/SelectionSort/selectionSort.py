data = [5,2,7,1,4,3,6] # big(O)~n**2
data_best=[1,2,3,4,5,6,7] # big(O)~n**2
data_worst=[7,6,5,4,3,2,1] # big(O)~n**2

def selection_sort (data):
    marker=0
    steps=0
    while marker<len(data):
        steps+=1
        for i in range(marker,len(data)):
            steps+=1
            if data[marker]>data[i]:
                data[marker],data[i]=data[i],data[marker]
        marker+=1
    print(steps)
    print(data)

selection_sort(data_worst)