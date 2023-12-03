def is_symbol(schematic, r, c, max_r, max_c):
    if not (0 <= r < max_r and 0 <= c < max_c):
        return False
    return schematic[r][c] not in ".0123456789"

with open("day_3/day_3.in") as file:
    schematic = [line.strip() for line in file]

rows, cols = len(schematic), len(schematic[0])
sum_parts = 0

for i, line in enumerate(schematic):
    j = 0
    while j < cols:
        if line[j].isdigit():
            start = j
            num_str = ""

            while j < cols and line[j].isdigit():
                num_str += line[j]
                j += 1

            num = int(num_str)

            if is_symbol(schematic, i, start-1, rows, cols) or is_symbol(schematic, i, j, rows, cols):
                sum_parts += num
            else:
                for adj in range(start-1, j+1):
                    if is_symbol(schematic, i-1, adj, rows, cols) or is_symbol(schematic, i+1, adj, rows, cols):
                        sum_parts += num
                        break
        else:
            j += 1

print(sum_parts)