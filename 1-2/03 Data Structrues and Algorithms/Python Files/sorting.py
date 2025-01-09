def insertion_sort(l0):
    l = l0
    for i in range(1, len(l)):
        val = l[i]
        j = i - 1
        while j >= 0 and l[j] > val:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = val
    return l
        
def bubble_sort(l0):
    l = l0
    swapped = 0

    while swapped == 0:
        swapped = 1
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                swapped = 0
                temp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = temp
            
    return l

def selection_sort(l0):
    l = l0
    for i in range(len(l0) - 1, 0, -1):
        lar_ind = i 
        for j in range(i):
            if l[j] > l[lar_ind]:
                lar_ind = j
        temp = l[lar_ind]
        l[lar_ind] = l[i]
        l[i] = temp
    
    return l

def merge(l1, start, mid, end):
    start1, start2 = start, mid
    lo = []

    while start1 < mid and start2 < end:
        if l1[start1] <= l1[start2]:
            lo.append(l1[start1])
            start1 += 1
        else:
            lo.append(l1[start2])
            start2 += 1

    while start1 < mid:
        lo.append(l1[start1])
        start1 += 1

    while start2 < end:
        lo.append(l1[start2])
        start2 += 1

    for i in range(len(lo)):
        l1[start + i] = lo[i]        

def merge_sort(l0, start, end):
    if end - start <= 1:
        return
    
    mid = start + (end - start)//2

    merge_sort(l0, start, mid)
    merge_sort(l0, mid, end)
    merge(l0, start, mid, end)


l = [90,45,6,12,1]

print("Insertion Sort:", insertion_sort(l))
print("Bubble Sort:", bubble_sort(l))
print("Selection Sort:",selection_sort(l))
merge_sort(l, 0 , len(l))
print("Merge Sort:", l)

