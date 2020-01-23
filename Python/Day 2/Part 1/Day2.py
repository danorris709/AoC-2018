def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    two_char_lines = 0
    three_char_lines = 0

    for line in lines:
        character_counter = get_char_counts(line)
        found_threes = False
        found_twos = False

        for key in character_counter.keys():
            found = character_counter[key]

            if found == 3 and not found_threes:
                three_char_lines += 1
                found_threes = True

            if found == 2 and not found_twos:
                two_char_lines += 1
                found_twos = True

    checksum = two_char_lines * three_char_lines
    print(checksum)


def get_char_counts(line):
    character_counter = {}

    for c in list(line):
        current_num_found = character_counter.get(c)

        if current_num_found is None:
            character_counter[c] = 1
            continue

        character_counter[c] = current_num_found + 1

    return character_counter


if __name__ == '__main__' :
    main()

