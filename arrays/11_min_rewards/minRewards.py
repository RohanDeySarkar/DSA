# naive sol => O(n^2) time | O(n) space
def minRewards(arr):
   rewards = [1 for _ in arr]
   for i in range(1, len(arr)):
       prevIdx= i-1
       if arr[i] > arr[prevIdx]:
           rewards[i] = rewards[prevIdx] + 1
       else:
           while arr[prevIdx] > arr[prevIdx + 1] and prevIdx >= 0:
               rewards[prevIdx] = max(rewards[prevIdx], rewards[prevIdx+1] + 1) 
               prevIdx -= 1
   return sum(rewards)

def minRewards(arr):
    rewards = [1 for _ in arr]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(arr)-1)):
        if arr[i] > arr[i+1]:
            rewards[i] = max(rewards[i+1] + 1, rewards[i])

    return sum(rewards)

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))
