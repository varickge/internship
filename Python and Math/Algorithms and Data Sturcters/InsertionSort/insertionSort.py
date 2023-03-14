data=[5,1,7,4,3,2,6] # big(O)~n**2 (1)
data_best=[1,2,3,4,5,6,7] # big(O)~n**2>(1), (2)
data_worst=[7,6,5,4,3,2,1] # big(O)~n**2>(2), (3)

def insertion_sort(data):
    steps=0
    for i in range(1,len(data)):
        steps+=1
        while data[i-1]>data[i] and i>0:
            steps+=1
            data[i],data[i-1]=data[i-1],data[i]
            i-=1
    print(steps)
    print(data)

insertion_sort(data)