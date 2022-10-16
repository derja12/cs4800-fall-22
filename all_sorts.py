import random
import math
import sys

class Counter:
    def __init__(self):
        self.mC = 0
        self.mS = 0
        
def Bubble(L,c):
    indicator = True
    while indicator == True:
        indicator = False
        for i in range(0,len(L)-1):
            c.mC += 1
            if L[i] > L[i+1]:
                c.mS += 1
                L[i],L[i+1] = L[i+1],L[i]
                indicator = True
    return

def Shaker(L,c):
    counter = 0
    indicator = True
    while indicator:
        indicator = False
        for i in range(0,len(L)-1):
            counter += 1
            c.mC += 1
            if L[i] > L[i+1]:
                c.mS += 1
                L[i],L[i+1] = L[i+1],L[i]
                indicator = True
        for i in range(len(L)-2, -1, -1):
            counter += 1
            c.mC += 1
            if L[i] > L[i+1]:
                c.mS += 1
                L[i],L[i+1] = L[i+1],L[i]
                indicator = True
    return
    
def Select(A,c):
    for i in range(len(A)):
        smallest = A[i]
        smallestIndex = i
        for i2 in range(i,len(A)):
            c.mC += 1
            if smallest > A[i2]:
                smallest = A[i2]
                smallestIndex = i2
        c.mS += 1
        A[i],A[smallestIndex] = A[smallestIndex],A[i]
    return
    
def createRandomSpecificList(Length,Min,Max):
    newList = []
    for i in range(0,Length):
        newList.append(random.randint(Min,Max))
        
    return newList

def createRandomList(size):
    A = []
    for i in range(size):
        r = random.randrange(0,size)
        A.append(r)
        
    return A

def Merge(A,c):
    if len(A) <= 1:
        return
    L = A[0:len(A)//2]
    R = A[len(A)//2:]
    c.mS += len(A)
    Merge(L,c)
    Merge(R,c)
    A.clear()
    while len(L) > 0 or len(R) > 0:
        c.mC += 1
        if len(L) == 0:
            A.append(R[0])
            R.remove(R[0])
            c.mS += 1
        elif len(R) == 0:
            A.append(L[0])
            L.remove(L[0])
            c.mS += 1
        elif L[0] < R[0]:
            A.append(L[0])
            L.remove(L[0])
            c.mS += 1
        else:
            A.append(R[0])
            R.remove(R[0])
            c.mS += 1
        
def mQuick(A,c):
    Quicksort(A,0,len(A)-1,c,True)
    
def Quick(A,c):
    Quicksort(A,0,len(A)-1,c,False)
    
def Quicksort(A,low,high,c,modified):
    if high-low <= 0:
        return
    if modified:
        mid = (low+high)//2
        c.mS += 1
        A[mid],A[low] = A[low],A[mid]
    
    pivot = low
    lmgt = pivot + 1
    
    for i in range(low + 1, high + 1):
        c.mC += 1
        if A[i] < A[pivot]:
            c.mS += 1
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt - 1
    c.mS += 1
    A[low],A[pivot] = A[pivot],A[low]
    
    Quicksort(A,low,pivot-1,c,modified)
    Quicksort(A,pivot+1,high,c,modified)

def Count(A,c):
    # F = []
    # for i in range(len(A)):
    #     F.append(0)
    
    F = [0] * len(A)
    
    for x in A:
        F[x] += 1
    
    count = 0
    for i in range(len(F)):
        if F[i] != 0:
            for k in range(F[i]):
                A[count] = i
                count += 1
                
    c.mC = len(A)
    c.mS = len(A)
                
def main1():
    sys.setrecursionlimit(5000)
    
    c = Counts()
    A = createRandomList(15)
    B = A[:]
    C = A[:]
    D = A[:]
    E = A[:]
    F = A[:]
    G = A[:]
    T = A[:]
    T.sort()
    print('List created:\n' + str(A) + '\n')
    Bubble(A,c)
    print('After BUBBLE:\n' + str(A) + '\n')
    Shaker(B,c)
    print('After SHAKER:\n' + str(B) + '\n')
    Select(C,c)
    print('After SELECTION:\n' + str(C) + '\n')
    Merge(D,c)
    print('After MERGE:\n' + str(D) + '\n')
    Quick(E,c)
    print('After QUICKSORT:\n' + str(E) + '\n')
    mQuick(F,c)
    print('After MODIFIEDQUICKSORT:\n' + str(F) + '\n')
    Count(G,c)
    print('After COUNTING:\n' + str(G) + '\n')
    print('SOLUTION:\n' +str(T) + '\n')
    
    
    
    
    if A != T:
        print('Error in sorting method BUBBLE')
    
    if B != T:
        print('Error in sorting method SHAKER')
        
    if C != T:
        print('Error in sorting method SELECTION')
    
    if D != T:
        print('Error in sorting method MERGE')

    if E != T:
        print('Error in sorting method QUICKSORT')

    if F != T:
        print('Error in sorting method MODIFIEDQUICKSORT')
    
    if G != T:
        print('Error in sorting method COUNTING')
    
    
    print('-------------------------------------')

def main2():
    section = ['Compares', 'Swaps', 'ComparesSorted']
    for i in range(3):
        print(section[i])
        sorters = [Bubble, Shaker, Select, Merge, Quick, mQuick, Count]
        end1 = " "
        print("%7s" % ("Size"), end=end1)
        for sort in sorters:
            print("%7s" % (sort.__name__), end=end1)
        print()
        
        for s in range(3,13):
            size = 2 ** s
            print("%7s" % (str(s) + " "), end=end1)
            for sort in sorters:
                A = createRandomList(size)
                if i == 2:
                    A.sort()
                    A[0],A[len(A)//2] = A[len(A)//2],A[0]
                B = A[:]
                A.sort()
                c = Counts()
                sort(B,c)
                if A != B:
                    print('Error!')
                logValue = 0
                if i == 0:
                    if c.mC > 0:
                        logValue = math.log(c.mC, 2)
                if i == 1:
                    if c.mS > 0:
                        logValue = math.log(c.mS, 2)
                if i == 2:
                    if c.mC > 0:
                        logValue = math.log(c.mC, 2)
                    
                print("%7.2f" % (logValue), end=end1)
            print()
            
            # create lists with size = size and use the class
        # to log base 2, value = math.log(int, 2)
        # print("%6.2f" % (value), end="")
        # end="" prints nothing at the end the the print statement (no line return)
        # %6.2f == six spaces wide, 2 digits after the decimal

if __name__ == '__main__':
    main1()
    main2()    
    
"""              Random   | Mostly sorted |   Swaps   |     Notes
    BIG O's               |               |           |   Easy to code
    -Bubble       N^2     |      N^2      |           |   
    -Shaker       N^2     |       N       |           |
    -Selection    N^2     |      N^2      |     N     |
    -Quick       N*logN   |      N^2      |           |
    -ModQuick    N*logN   |     N*logN    |           |   
    -Merge       N*logN   |     N*logN    |           |
    -Counting      N      |       N       |           |   Limited use  
"""