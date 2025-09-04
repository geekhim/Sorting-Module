def bubble_sort(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst

def insertion_sort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while j>=0 and lst[j]>key:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key   
    return lst

def merge_sort(lst,low,high):
    if low==high:
        return [lst[low]]
    mid=(low+high)//2
    left_half=merge_sort(lst,low,mid)
    right_half=merge_sort(lst,mid+1,high)
    return merge(left_half,right_half)
def merge(left,right):
    sort_list=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sort_list.append(left[i])
            i+=1
        else:
            sort_list.append(right[j])
            j+=1
    while i<len(left):
        sort_list.append(left[i])
        i+=1
    while j<len(right):
        sort_list.append(right[j])
        j+=1
    return sort_list
    

def selection_sort(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst