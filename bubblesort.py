bs = [82,56,23,18,79]

for a in range(0,4):
    for i in range(0,4):
        if bs[i] > bs[i + 1]:
            swap = bs[i]
            bs[i] = bs[i + 1]
            bs[i + 1] = swap
print bs


#def bubbleSort(alist):
#    for passnum in range(len(alist)-1,0,-1):
#        for i in range(passnum):
#            if alist[i]>alist[i+1]:
#                temp = alist[i]
#                alist[i] = alist[i+1]
#                alist[i+1] = temp

#alist = [82,56,23,18,79]
#bubbleSort(alist)
#print(alist)