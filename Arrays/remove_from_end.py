# remove from the last position in the array if the array
# is not empty (i.e. length is non-zero)

# def removeEnd(arr, length):
#     if length > 0:
#         arr[length -1] = 0
#         del arr[-1]
#         print(arr)
#
# arr = [4,3,2]
# print(arr)
#
# removeEnd(arr, len(arr))



def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index -1] = arr[index]
    arr.pop() #is there any alternative way to do that?
    print(arr)

arr =  [4,5,6, 5, 2,4, 7, 12, 44]
i = 4 #target index

removeMiddle(arr, i, len(arr))

