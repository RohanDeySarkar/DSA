def peaks(arr):
    peaks = []
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue
        peaks.append(arr[i])
        i += 1
    return peaks

arr = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(peaks(arr))
