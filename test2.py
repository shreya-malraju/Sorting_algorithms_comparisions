import random
from heap_sort import heapsort
from merge_sort import mergesort
import time
from matplotlib import pyplot as plt

l=1
length=1
inc=1
ans=[[] for i in range(0,2)]
sz=[]
while(True):
    arr=[random.randint(0,l) for i in range(0,l) ]
    print(arr)
    print(len(arr))
    temp=arr[:]
    st=time.time()
    mergesort(temp)
    en=time.time()
    ans[0].append(en-st)
    st=time.time()
    heapsort(arr)
    en=time.time()
    ans[1].append(en-st)
    sz.append(l)
    l+=inc
    if(ans[1][-1]-ans[0][-1]>1):
        break
    if(l>length*10):
        length*=10
        inc*=10
labels=["merge sort","heap sort"]
for tc, label in zip(ans, labels):
    plt.plot(sz,tc, label=label)
plt.legend()
plt.show()