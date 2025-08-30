def linear_search(input: list[int], search_term: int) -> int | None:
    for i in range(len(input)):
        if input[i] == search_term:
            return i
    return None


def binary_search(input: list[int], search_term: int) -> int | None:
    left = 0
    right = len(input) - 1

    while left <= right:
        index = (left + right) // 2
        if input[index] == search_term:
            return index
        elif search_term < input[index]:
            right = index - 1
        else:
            left = index + 1

    return None


def _check_input_types(input: list) -> bool:
    for item in input:
        if type(item) not in (int, float):
            return False
    return True


def bubble_sort(nums: list[int | float]) -> tuple[int | float]:
    if not _check_input_types(input=nums):
        return "Incorrect input types"
    nums = list(nums)
    for num in nums:
        for j in range(len(nums) - 1):
            left = nums[j]
            right = nums[j + 1]
            if left > right:
                nums[j], nums[j + 1] = right, left
    return nums


def insertion_sort(nums: list[int | float]) -> list[int | float]:
    if not _check_input_types(input=nums):
        return "Incorrect input types"
    nums = list(nums)
    output = []

    for num in nums:
        if not output:
            output.append(num)
            continue
        for i in range(len(output)):
            if num < output[i]:
                output.insert(i, num)
                break
        else:
            output.append(num)

    return output


sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
unsorted_list = [12, 19, 5, 14, 17, 8, 15, 18, 9, 6, 11, 2, 1, 16, 13, 0, 3, 7, 4, 10]

print("Bubble Sort:", bubble_sort(nums=unsorted_list))
print("Insertion Sort: ", insertion_sort(unsorted_list))
print("Linear Search:", linear_search(input=unsorted_list, search_term=13))
print("Linear Search:", linear_search(input=unsorted_list, search_term=10))
print("Binary Search: ", binary_search(input=sorted_list, search_term=14))
print("Binary Search: ", binary_search(input=sorted_list, search_term=42))
