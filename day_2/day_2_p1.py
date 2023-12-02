with open("day_2/day_2.in") as file_input:
    game_data_lines = file_input.read().strip().split("\n")

total_score = 0

for line in game_data_lines:
    game_description, cube_data = line.split(": ")
    game_id = int(game_description.split(" ")[1])

    is_game_possible = True
    for cube_set in cube_data.split("; "):
        for cube in cube_set.split(", "):
            cube_count, cube_color = cube.split(" ")
            cube_count = int(cube_count)

            if cube_color == "red" and cube_count > 12:
                is_game_possible = False
                break
            if cube_color == "green" and cube_count > 13:
                is_game_possible = False
                break
            if cube_color == "blue" and cube_count > 14:
                is_game_possible = False
                break

    if is_game_possible:
        total_score += game_id

print(total_score)