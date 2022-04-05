def findMedian(arr):
    arr.sort()
    if len(arr)%2==0:
        left_mp = int((len(arr)/2))
        right_mp = int((len(arr)/2))+1
        # midpoint = arr[left_mp]
        midpoint = (arr[left_mp]+arr[right_mp])/2
        return midpoint
    else:
        right_mp = int((len(arr)/2)+0.5)
        midpoint = arr[right_mp]
        return midpoint
    # return arr
