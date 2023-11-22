import ctools

def main():
    priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    raw_data = ctools.wopen("day3.d")
    rucksacks = raw_data.strip().split("\n")
    total = 0
    for ruck in rucksacks:
        # print(ruck)
        # single division returns a float, therefore, type error.
        compartment_split = len(ruck)//2
        # print(compartment_split)
        compartment0 = set(ruck[:compartment_split])
        compartment1 = set(ruck[compartment_split:])
        for i in compartment0:
            if i in compartment1:
                value = priority.index(i) + 1
        total += value
    # part 1 
    print(total)
    # part 2
    total = 0
    count = 0
    three_elves = []
    for ruck in rucksacks:
        count += 1
        three_elves.append(ruck)
        # print(count)
        if count == 3:
            count = 0
            first_elf = set(three_elves[0])
            second_elf = set(three_elves[1])
            third_elf = set(three_elves[2])
            for letter in first_elf:
                if (letter in second_elf) and (letter in third_elf):
                    # print(letter, second_elf, third_elf)
                    total += priority.index(letter) + 1
            three_elves = []
    print(total)



if __name__ == "__main__":
    main()
