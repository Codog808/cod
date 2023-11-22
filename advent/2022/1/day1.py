import ctools 

data = ctools.wopen("day1.d")
def main():
    # part 1
    elf_calories = data.split("\n\n")
    highscore = 0
    second = 0
    third = 0
    # scores = []
    for elf in elf_calories:
        total_calories = elf.strip().split("\n")
        # print(total_calories, elf)
        total = 0
        for calories in total_calories:
            total += int(calories)
        if total > highscore:
            third = second
            second = highscore
            highscore = total
            

    print(highscore)

    # part 2
    #print(highscore, second, third)
    print(highscore + second + third)

def clean():
    """
    Data:
    8000
    3000

    2000
    3233
    2343
    """
    each_elf_calories = [
            sum(
                int(x) for x in i.strip().split("\n")   # generator sum
                ) 
                    for i in data.strip().split("\n\n") # right to left
            ]                                           # list comp

    print(each_elf_calories)
    # part 1 answer
    print(max(each_elf_calories))

    # part 2 answer
    greatest_to_least = sorted(each_elf_calories, reverse=True)
    print( sum( [greatest_to_least[i] for i in range(3)] ) )

    ### with the help of chatgpt
    # other part 1 
    max_value = each_elf_calories[0]
    for elf_calories in each_elf_calories:
        if elf_calories > max_value:
            max_value = elf_calories
    # other part 2          bubble sort
    length_of_list = len(each_elf_calories)
    for i in range(length_of_list):
        for j in range(0, length_of_list-i-1):  
            if each_elf_calories[j] > each_elf_calories[j+1]:
                each_elf_calories[j], each_elf_calories[j+1] = each_elf_calories[j+1], each_elf_calories[j] 


if __name__ == "__main__":
    # main()
    clean()
