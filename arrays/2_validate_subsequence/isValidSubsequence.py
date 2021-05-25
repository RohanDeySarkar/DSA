def isValidSubsequence(arr, seq):
    seqIdx = 0
    arrIdx = 0
    while arrIdx < len(arr) and seqIdx < len(seq):
        if arr[arrIdx] == seq[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(seq)


arr = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]
print(isValidSubsequence(arr, seq))
