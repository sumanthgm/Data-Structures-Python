

def sarch(key,arr):
    low = 0
    high = len(arr)//2
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]==key):
            return mid
        elif key>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1

nums = [2,4,6,8,10,12,14,16]
key = int(input("Enter Key : "))
print("Ans Is",sarch(key,nums))
