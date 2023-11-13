    def quick_srot(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            more = [x for x in arr[1:] if x > pivot]
            return  quick_srot(less)+[pivot]+quick_srot(more)


    arr=[9,0,2,6,3,8,4,9,6,3,1,3]
    sort_arr=quick_srot(arr)
    print(sort_arr)