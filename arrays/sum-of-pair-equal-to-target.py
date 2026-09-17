from typing import List


def two_sum(arr: List[int], target: int) -> bool:
    length = len(arr)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == target:
                return True

    return False

def two_sum_using_two_pointer(arr: List[int], target: int) -> bool:
    sorted_array = sorted(arr)
    left, right = 0, len(sorted_array) - 1

    while left < right:

        sum = sorted_array[left] + sorted_array[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False

if two_sum([0, -1, 2, -3, 1], -2):
    print("Get in jhor")
else:
    print("Nth for you")

if two_sum_using_two_pointer([0, -1, 2, -3, 1], -2):
    print("Get in jhor")
else:
    print("Nth for you")
