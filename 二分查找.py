def search(l, val):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = low + (high - low)//2
        if l[mid] > val:
            high = mid - 1
        elif l[mid] < val:
            low = mid + 1
        else:
            return True
    return False


l = [1, 5, 7, 11, 17, 22, 38, 55]
print(search(l, 22))

