import cProfile
import math
def get_size(list_of_values):
    n = int(math.sqrt(len(list_of_values)))
    return n



def draw_row(data_list):
    str_i = "│"
    for data in data_list:
        if len(data) == 0:
            str_i += "----│"
        elif len(data) == 1:
            str_i += "--" + data + "-│"
        elif len(data) == 2:
            str_i += "-" + data + "-│"
    return str_i



def draw_grid(n):
    top_border = "┌───" + "┬───" * (n-1) + "┐"

    middle_rows = ""
    for i in range(n):
        row = "│"
        for j in range(n):
            row += " x "
            if j < n-1:
                row += "│"
        row += "│"
        middle_rows += row + "\n"
        if i < n-1:
            middle_rows += "├───" + "┼───" * (n-1) + "┤\n"

    bottom_border = "└───" + "┴───" * (n-1) + "┘"

    grid_str = top_border + "\n" + middle_rows + bottom_border
    print(grid_str)



def get_input(list_of_valid_choices):
    while True:
        choice = input("Enter a value: ")
        if choice == "quit":
            return "quit"
        elif choice in list_of_valid_choices:
            return choice
        else: 
            print(end="")



def is_vertically_adjacent(n, first, second):
    return abs(first - second) == n



def is_horizontally_adjacent(n, first, second):
    return first // n == second // n and abs(first - second) == 1



def swap_tile(list_of_tiles, tile_choice):
        empty_index = list_of_tiles.index('')
        tile_index = list_of_tiles.index(tile_choice)
        list_of_tiles[empty_index], list_of_tiles[tile_index] = \
            list_of_tiles[tile_index], list_of_tiles[empty_index]



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