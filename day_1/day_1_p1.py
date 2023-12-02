with open("day_1/day_1.in") as file_input:
    data = file_input.read()

total_sum = 0

for line in data.strip().split():
    first_digit = None
    last_digit = None
    for character in line:
        if character.isdigit():
            if first_digit is None:
                first_digit = character
            last_digit = character

    combined_number = int(first_digit + last_digit)
    total_sum += combined_number

print(total_sum)