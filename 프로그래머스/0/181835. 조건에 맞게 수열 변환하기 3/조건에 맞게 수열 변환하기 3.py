def solution(arr, k):
    if (k%2 == 1):
        for i in range(0,len(arr)):
            arr[i] = arr[i]*k
    else:
        for i in range(0,len(arr)):
            arr[i] = arr[i]+k
    return arr