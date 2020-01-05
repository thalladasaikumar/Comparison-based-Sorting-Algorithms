from math import floor
import random
import time
import sys
import matplotlib.pyplot as plot
from cProfile import label
from statistics import mean

#------------------ InsertionSort --------------#
def insersionSort(array):
    for i in range(1, len(array)): 
        j = i-1
        key = array[i]
        while j>=0 and array[j]>key:
            array[j+1] = array[j]
            j = j-1
        
    array[j+1]=key
#-----------------------------------------------#

#------------------- Merge Sort ----------------#
def merge_sort(arr):
    if len(arr)>1:
        m = len(arr)//2
        leftArr = arr[:m]
        rightArr = arr[m:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i=0
        j=0
        k=0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k]=leftArr[i]
                i=i+1
            else:
                arr[k]=rightArr[j]
                j=j+1
            k=k+1

        while i < len(leftArr):
            arr[k]=leftArr[i]
            i=i+1
            k=k+1

        while j < len(rightArr):
            arr[k]=rightArr[j]
            j=j+1
            k=k+1
    return (arr)
#----------------------------------------------------------#

# Heap Sort-----------------------------------------------#
mainHeap=[]
arrSize=0
sortedArr=[]

def create_heap(array):
    global mainHeap
    mainHeap = [0] * (len(array)+1)
    for i in range(0,len(array)):
        insert(array[i]);

def insert(x):
    global arrSize
    arrSize = arrSize +1
    y=arrSize
    mainHeap[y]=x
    bubble_up(y)

def bubble_up(pos):

    PID = pos // 2;

    CID = pos;
    while (CID > 0 and mainHeap[PID] > mainHeap[CID]):

        swap(CID, PID);
        CID = PID;
        PID = PID // 2;


def swap(a,b):
    temp = mainHeap[a];
    mainHeap[a] = mainHeap[b];
    mainHeap[b] = temp;



def heap_sort1(array):
    create_heap(array);


def extract_min():
    global arrSize
    min = mainHeap[1]
    mainHeap[1]=mainHeap[arrSize]
    mainHeap[arrSize] = 0
    sinkDown(1)
    arrSize=arrSize -1
    return min

def sinkDown(k):
    small = k

    LCID = 2 * k
    RCID = 2 * k + 1
    if (LCID < arrSize  and mainHeap[small] > mainHeap[LCID]):
        small = LCID

    if (RCID < arrSize  and mainHeap[small] > mainHeap[RCID]):
        small = RCID

    if (small != k):
        swap(k, small)
        sinkDown(small)



def heap_sort(array):
    sortedArr=[0]*len(array)
    heap_sort1(array)
    for i in range(0,len(array)):
        sortedArr[i]=extract_min()

    return sortedArr
#--------------------------------------------------------#

# In Place Quick Sort ------------------------------------#
import random

def partition(arr, low, high):
    i = (low - 1)

    pivot = arr[random.randint(low,high)]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def quick_sort(numbers):
    arr = numbers
    n = len(arr)
    quickSort(arr, 0, n - 1)
    return arr
#-------------------------------------------------------#
#----------- Median Quick Sort -------------------------#
medianC = 0
def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c


def partition_median(array, smallValArr, highValArr):
    small = array[smallValArr]
    high = array[highValArr - 1]
    length = highValArr - smallValArr
    middle = array[smallValArr + length // 2]

    pivot = median(small, high, middle)

    pivotindex = array.index(pivot)

    array[pivotindex] = array[smallValArr]
    array[smallValArr] = pivot

    i = smallValArr + 1
    for j in range(smallValArr + 1, highValArr):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    highEndVal = array[smallValArr]
    array[smallValArr] = array[i - 1]
    array[i - 1] = highEndVal
    return i - 1


def quicksort_median(array, smallIndex, highIndex):
    global medianC
    if smallIndex+ 10  <= highIndex:
        newpivotindex = partition_median(array, smallIndex, highIndex)

        medianC += (highIndex - smallIndex - 1)
        quicksort_median(array, smallIndex, newpivotindex)

        quicksort_median(array, newpivotindex + 1, highIndex)

    else:
        insertion_sortt(array,smallIndex,highIndex)

def insertion_sortt(array,a,b):
    for i in range(a, b):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            j = j - 1

def mquick_sort(inputArr):
    quicksort_median(inputArr, 0, len(inputArr))
    return inputArr
#--------------------------------------------------------------#


if __name__ == '__main__':
    _programStartTime = time.time()
    sys.setrecursionlimit(10**6)
    arr = [1000,2000,3000,4000,5000,10000,20000,30000,40000,50000] # x-axis ticks for input quantity
    yTicks_insertion_sort = [] #plot y axis ticks
    yTicks_merge_sort = []
    yTicks_inplaceQuick_sort = []
    yTicks_medianQuick_sort = []
    yTicks_heap_sort = []
    
    for index in range(0, len(arr)):
        runs = 1
        time_insertion_sort = []
        time_merge_sort = []
        time_inplaceQuick_sort = []
        time_medianQuick_sort = []
        time_heap_sort = []
        
        #while runs < 4:
        sortedArray = []
        for a in range(0,arr[index]):
            sortedArray.append(a)
        _startTime = time.time()
        insersionSort(sortedArray[:])
        _endTime = time.time()
        time_insertion_sort.append((_endTime-_startTime)*1000)
        
        _startTime = time.time()
        merge_sort(sortedArray[:])
        _endTime = time.time()
        time_merge_sort.append((_endTime-_startTime)*1000)
        
        _startTime = time.time()
        quick_sort(sortedArray[:])
        _endTime = time.time()
        time_inplaceQuick_sort.append((_endTime-_startTime)*1000)
        
        _startTime = time.time()
        mquick_sort(sortedArray[:])
        _endTime = time.time()
        time_medianQuick_sort.append((_endTime-_startTime)*1000)            

        _startTime = time.time()
        heap_sort(sortedArray[:])
        _endTime = time.time()
        time_heap_sort.append((_endTime-_startTime)*1000)            
            
         #   runs = runs+1
        
        yTicks_insertion_sort.append(mean(time_insertion_sort))
        yTicks_merge_sort.append(mean(time_merge_sort))
        yTicks_inplaceQuick_sort.append(mean(time_inplaceQuick_sort))
        yTicks_medianQuick_sort.append(mean(time_medianQuick_sort))
        yTicks_heap_sort.append(mean(time_heap_sort))
        
#     print("Program end time : ",(time.time()-_programStartTime)*1000)
    
    print("Array size: ,","insertion Sort: ,","Merge Sort: ,","Heap Sort: ,","InplaceQuick Sort: ,","MedianQuick Sort: ")
    for i in range(0,len(arr)):
        print(arr[i],",",yTicks_insertion_sort[i],",",yTicks_merge_sort[i],",",yTicks_heap_sort[i],",",yTicks_inplaceQuick_sort[i],",",yTicks_medianQuick_sort[i])
    
    plot.plot(arr, yTicks_insertion_sort,'g', label='Insertion Sort')
    plot.plot(arr, yTicks_merge_sort,'y', label='Merge Sort')
    plot.plot(arr, yTicks_inplaceQuick_sort,'b', label='In-Place Quick Sort')
    plot.plot(arr, yTicks_medianQuick_sort,'r', label='Median Quick Sort')
    plot.plot(arr, yTicks_heap_sort,'k', label='Heap Sort')
    plot.xlabel('Input Data Size')
    plot.ylabel('Time for sorting(milli seconds)')
    plot.legend(loc='upper left')
    
    plot.show()