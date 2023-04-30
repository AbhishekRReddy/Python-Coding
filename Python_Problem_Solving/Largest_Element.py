
def largest( arr, n):
    largest = float('-inf')
    for elem in arr:
        if elem > largest:
            largest = elem
    return largest