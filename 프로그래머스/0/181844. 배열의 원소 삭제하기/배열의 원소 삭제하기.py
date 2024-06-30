def solution(arr, delete_list):
    for i in delete_list:
        try:
            arr.remove(i)
        except ValueError:
            print("없음")
            
    return arr