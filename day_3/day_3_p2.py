def update_gears(schematic, r, c, num, rows, cols, gears):
    if not (0 <= r < rows and 0 <= c < cols):
        return False

    if schematic[r][c] == "*":
        gears[r][c].append(num)
    return schematic[r][c] not in ".0123456789"

with open("day_3/day_3.in") as file:
    schematic = file.read().strip().split("\n")

rows, cols = len(schematic), len(schematic[0])
gear_nums = [[[] for _ in range(cols)] for _ in range(rows)]
gear_ratio_sum = 0

for i, line in enumerate(schematic):
    j = 0
    while j < cols:
        if line[j].isdigit():
            start = j
            part_num = ""

            while j < cols and line[j].isdigit():
                part_num += line[j]
                j += 1

            part_num = int(part_num)

            update_gears(schematic, i, start-1, part_num, rows, cols, gear_nums)
            update_gears(schematic, i, j, part_num, rows, cols, gear_nums)

            for adj in range(start-1, j+1):
                update_gears(schematic, i-1, adj, part_num, rows, cols, gear_nums)
                update_gears(schematic, i+1, adj, part_num, rows, cols, gear_nums)
        else:
            j += 1

for i in range(rows):
    for j in range(cols):
        if schematic[i][j] == "*" and len(gear_nums[i][j]) == 2:
            gear_ratio_sum += gear_nums[i][j][0] * gear_nums[i][j][1]

print(gear_ratio_sum)
