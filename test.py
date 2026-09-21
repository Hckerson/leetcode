x = [0, 1, 0, 3, 12]
[1, 1, 0, 3, 12]
[1, 3, 0, 3, 12]
[1, 3, 12, 3, 12]
count = 0
y = [num for num in x if count_and_increment(num)]


def count_and_increment(num):
    if num > 0:
        return True
    count += 1
    return False


print()
