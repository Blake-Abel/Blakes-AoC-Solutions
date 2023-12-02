with open("day_2/day_2.in") as file_input:
    game_data_lines = file_input.read().strip().split("\n")

total_score = 0

for line in game_data_lines:
    game_description, cube_data = line.split(": ")

    red = 0
    green = 0
    blue = 0

    for cube_set in cube_data.split("; "):
        for cube in cube_set.split(", "):
            cube_count, cube_color = cube.split(" ")
            cube_count = int(cube_count)

            if cube_color == "red":
                red = max(red, cube_count)
            if cube_color == "green":
                green = max(green, cube_count)
            if cube_color == "blue":
                blue = max(blue, cube_count)

    total_score +=red * green * blue

print(total_score)