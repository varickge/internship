data = [1,5,2,4,3,8,10] # big(O)~n**2
data_best=[1,2,3,4,5,8,10]# big(O)=n
data_worst=[10,8,5,4,3,2,1] # big(O)=n**2

def bubble_sort(data):
    steps=0
    swap=True
    while swap:
        steps+=1
        swap = False
        for i in range(len(data)-1):
            steps+=1
            if data[i]>data[i+1]:
                data[i], data[i+1] = data[i+1],data[i]
                swap=True
    print(steps)
    print(data)

bubble_sort(data_worst)
