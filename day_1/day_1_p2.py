with open("day_1\day_1.in") as file_input:
    data = file_input.read()

total_calibration_value = 0
number_words = ["one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine"]

for line in data.strip().split():
    first_digit = None
    last_digit = None

    for index in range(len(line)):
        current_digit = None

        character = line[index]
        if character.isdigit():
            current_digit = int(character)

        for word_index, word in enumerate(number_words):
            if line[index:(index + len(word))] == word:
                current_digit = word_index + 1
                break

        if current_digit:
            if first_digit is None:
                first_digit = current_digit
            last_digit = current_digit

    total_calibration_value += first_digit * 10 + last_digit

print(total_calibration_value)