
arr = [9,2,1,4,6]
a = len(arr) // 2
arr.sort()
if not len(arr) % 2:
    print((arr[a-1]+arr[a])/2)
print(arr[a])