def milestone_1(input_tiles):
    input_tiles = [int(tile) if tile != "" else None for tile in input_tiles.split(",")]
    input_size = int(len(input_tiles) ** 0.5)
    top_border = "┌────" + "┬────" * (input_size - 1) + "┐" 
    middle_rows = ""
    for i in range(input_size):
        row = "│"
        for j in range(input_size):
            tile_index = i * input_size + j
            tile = input_tiles[tile_index]
            if tile is not None:
                if tile < 10:
                    row += f"  {tile} "
                else:
                    row += f" {tile} "
            else:
                row += "    "
            if j < input_size - 1:
                row += "│"
        row += "│"
        middle_rows += row + "\n"
        if i < input_size - 1:
            middle_rows += "├────" + "┼────" * (input_size - 1) + "┤\n"

    bottom_border = "└────" + "┴────" * (input_size - 1) + "┘"

    grid_str = top_border + "\n" + middle_rows + bottom_border
    print(grid_str)

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


def main(tiles):
    milestone_1(tiles)
    if tiles.endswith(','):
        tiles += ','
        tiles = tiles.replace(",," , ",")
        tiles = list(map(str.strip, tiles.split(",")))
    else:
        tiles = tiles.replace(",," , ", ,")
        tiles = list(map(str.strip, tiles.split(",")))

    size = int(len(tiles) ** 0.5)
    blank_index = tiles.index("")

    moves = 0
    while True:
        if is_complete(tiles) == True:
            print(f"You won in {moves}. Congratulation")
            break
        move = input("Your move: ")
        if move == "quit":
            print("Goodbye!")
            return False

        elif move.isdigit():
            num = int(move)
            num_index = tiles.index(str(num))
            if abs(blank_index - num_index) == 1 and (blank_index // size) == (num_index // size) or \
               abs(blank_index - num_index) == size and (blank_index % size) == (num_index % size):
                tiles[blank_index], tiles[num_index] = tiles[num_index], tiles[blank_index]
                blank_index = num_index
                moves += 1
                milestone_1(",".join(tiles))
            else:
                print(f"{move} is not valid. Try again.")
        else:
            print(f"{move} is not valid. Try again.")
        
