def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    counter = 0
    found_counter = {}
    found = False

    while not found:
        for line in lines:
            int_value = int(line)
            counter += int_value

            if found_counter.get(counter) is not None:
                print(counter)
                found = True
                break

            found_counter[counter] = 1


if __name__ == '__main__' :
    main()

