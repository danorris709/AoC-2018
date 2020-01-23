def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    two_char_lines = 0
    three_char_lines = 0
    found_lines = []

    for line in lines:
        character_counter = get_char_counts(line)
        found_threes = False
        found_twos = False
        added_to_cache = False

        for key in character_counter.keys():
            found = character_counter[key]

            if found == 3 and not found_threes:
                if not added_to_cache:
                    found_lines += [line.splitlines()[0]]
                    added_to_cache = True

                three_char_lines += 1
                found_threes = True

            if found == 2 and not found_twos:
                if not added_to_cache:
                    found_lines += [line.splitlines()[0]]
                    added_to_cache = True

                two_char_lines += 1
                found_twos = True

    print(find_differing_pair_by_1(found_lines))


def get_char_counts(line):
    character_counter = {}

    for c in list(line):
        current_num_found = character_counter.get(c)

        if current_num_found is None:
            character_counter[c] = 1
            continue

        character_counter[c] = current_num_found + 1

    return character_counter


def find_differing_pair_by_1(lines):
    found_pair = False
    counter = 0
    pair = None

    while counter < len(lines) and not found_pair:
        line_chars = list(lines[counter])
        second_counter = 0

        while second_counter < len(lines) and not found_pair:
            next_line_chars = list(lines[second_counter])
            difference = 0

            for i in range(len(line_chars)):
                if line_chars[i] != next_line_chars[i]:
                    difference += 1

            if difference == 1:
                found_pair = True
                pair = lines[counter]

            second_counter += 1
        counter += 1

    if pair is None:
        raise Exception
    return pair


if __name__ == '__main__' :
    main()

