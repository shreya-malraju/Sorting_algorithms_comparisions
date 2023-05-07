from insertion_sort import insertionsort
from merge_sort import mergesort
import random
import time
import matplotlib.pyplot as plt

x_insertionsort = []
y_insertionsort = []
x_mergesort = []
y_mergesort = []
for k in range(1, 100, 5):
    array = [random.randint(1, 100) for i in range(k * 10)]
    array1 = array
    start = time.time()
    insertionsort(array)
    x_insertionsort.append(k * 10)
    y_insertionsort.append(round(time.time() - start, 5))
    start = time.time()
    mergesort(array1)
    x_mergesort.append(k * 10)
    y_mergesort.append(round(time.time() - start, 5))

plot1 = plt.plot(x_insertionsort, y_insertionsort, marker="o")
plot2 = plt.plot(x_mergesort, y_mergesort, marker="o")
plt.legend(["Insertion sort", "Merge sort"])
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()