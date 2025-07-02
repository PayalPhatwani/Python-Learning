def search(num,arr):
    low=0
    high=len(arr)-1
    result = -1
    
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]==num):
            return mid
        elif(arr[mid]>num):
            high=mid-1
        elif(arr[mid]<num):
            low=mid+1
    
    return result


print(search(5,[1,2,3,4,5]))           
            
            
    