from insertion_sort import insertion_sort


def merge_sort(A):

    if len(A) <= 7:
        insertion_sort(A)
        return A

    else:
        middle = len(A) // 2

        left = A[:middle]
        right = A[middle:]

        left = merge_sort(left)
        right = merge_sort(right)

    return merge(left, right)




def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


"""

numbers = [8, 3, 2, 9, 1, 2, 0, 1, 3, 10, -2, 77, 22, 34, 93]

print(merge_sort(numbers)) 

"""