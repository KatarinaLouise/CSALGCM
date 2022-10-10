# function to check how many swaps were done
# merge sort algorithm from digitalocean
def merge_sort(unsorted_array, length):
    swaps = 0
    if len(unsorted_array) > 1:
        mid = (len(unsorted_array) - 1) // 2  # Finding the mid of the array
        left = unsorted_array[:mid + 1]  # Dividing the array elements
        right = unsorted_array[mid + 1:]  # into 2 halves

        swaps += merge_sort(left, length)
        swaps += merge_sort(right, length)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
                swaps += len(left) - i
            k += 1

        # Checking if any element was left
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            swaps += len(left) - i
            j += 1
            k += 1

    return swaps


# main driver
n = int(input())
students = []
for i in range(n):
    students.append(int(input()))
print(merge_sort(students, len(students)))
