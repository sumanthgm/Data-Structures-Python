# linear search
def lsearch(arr,key):
    for i in range (len(arr)):
        if key == arr[i]:
            return i
    return -1


arr=[10,20,30,40,50]
key=int(input("Eneter the Key Input to search  :"))
res=lsearch(arr,key)
print(res)

