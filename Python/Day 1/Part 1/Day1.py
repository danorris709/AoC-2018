def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    counter = 0

    for line in lines:
        int_val = int(line)
        counter += int_val

    print(counter)


if __name__ == '__main__' :
    main()

