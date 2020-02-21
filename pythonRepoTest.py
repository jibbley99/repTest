class min:
    def findMin(arr):
        min = arr[0]
        for element in arr:
            if (element <= min):
                min = element 
        return min

    print(findMin([10, 9, 5, 8, 12, 3, 2]))