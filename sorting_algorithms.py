import random
import math
import sys

class Counts:
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

def createRandomList(n):
	l = []
	for i in range(n):
		l.append(random.randrange(0, n))
	return l	
    
def main1():
    sys.setrecursionlimit(5000)
    
    c = Counts()
    A = createRandomList(15)
    B = A[:]
    T = A[:]
    T.sort()
    print('List created:\n' + str(A) + '\n')
    Bubble(A,c)
    print('After BUBBLE:\n' + str(A) + '\n')
    Shaker(B,c)
    print('After SHAKER:\n' + str(B) + '\n')
    print('SOLUTION:\n' +str(T) + '\n')
    
    
    
    
    if A != T:
        print('Error in sorting method BUBBLE')
    
    if B != T:
        print('Error in sorting method SHAKER')
    print('-------------------------------------')

def main2():
    section = ['Compares', 'Swaps', 'ComparesSorted']
    for i in range(3):
        print(section[i])
        sorters = [Bubble, Shaker]
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
