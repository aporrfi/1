import math
def is_complete(list_of_tiles):
    n = int(math.sqrt(len(list_of_tiles)))

    if "" not in list_of_tiles:
        return False

    nums = []
    for tile in list_of_tiles:
        if tile == "":
            nums.append(None)
        else:
            nums.append(int(tile))

    sorted_nums = sorted([num for num in nums if num is not None])
    return nums[:len(sorted_nums)] == sorted_nums and len(nums) == n * n
print(is_complete(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15', '14', '']))