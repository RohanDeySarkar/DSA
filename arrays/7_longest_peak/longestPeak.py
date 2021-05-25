def longestPeak(arr):
    longestPeak = 0
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i-1] < arr[i] and arr[i] > arr[i+1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 1
        rightIdx = i + 1

        while leftIdx >= 0 and arr[leftIdx] > arr[leftIdx - 1]:
            leftIdx -= 1
        while rightIdx < len(arr) - 1 and arr[rightIdx] > arr[rightIdx + 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx + 1
        
        longestPeak = max(longestPeak, currentPeakLength)

        i = rightIdx
        
    return longestPeak


arr = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestPeak(arr))
