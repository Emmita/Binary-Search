list = [1, 2, 3, 4, 5, 6, 7, 8 , 9]

def search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        aux = list[mid]
        if aux == item:
           return mid
        if aux > item:
           high = mid -1
        else:
           low = mid + 1
    return None

print(search(list, 5)) # => 4
print(search(list, -5)) # => None
