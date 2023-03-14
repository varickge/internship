import time

def timer(n):
    time.sleep(1)
    print(n)
    if n<10:
        print("\a")
    if n==0:
        return
    else:
        timer(n-1)

timer(20)