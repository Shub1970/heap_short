def sub_heap(array, index):
    left = 2 * index + 1
    right = 2 * index + 2
    large = index             # initali index is the largest number
    if left<len(array) or right<len(array):
        if left<len(array) and array[left] > array[index]:
            large = left
        if right<len(array)and array[right] > array[large]:
            large = right
        if large != index:
            array[index], array[large] = array[large], array[index]
            sub_heap(array, large)
    else:
        return


def heap_create(array):
    last = (len(array) // 2)-1
    for i in range(last, -1, -1):
        sub_heap(array, i)
    return array
def heap_short(array):
    max_shorted_array=[]
    for i in range(len(array)-1,-1,-1):
        heap_create(array)
        array[0],array[-1]=array[-1],array[0]
        max_shorted_array.append(array[-1])
        array=array[0:i]
    return max_shorted_array




array = [2, 7, 5, 4, 3, 9, 8,1,2,3,4,5,6,7,8,9]
print(heap_short(array))

