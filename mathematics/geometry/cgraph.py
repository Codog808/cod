import math

def display(list_of_list):
    """Create an area of x by y"""
    for list in list_of_list:
        print(list)

def fill_in_list(x, y):
    list_of_list_made = []
    for i in range(y):
        j = ["x"] * x
        list_of_list_made.append(j)
    return list_of_list_made

def pad(string, width, filler="_"):
    return string.rjust(width, filler)

def draw(init_list_of_list, equal_list):
    x = len(init_list_of_list)
    y = len(init_list_of_list[0])
    a = len(equal_list)
    place_length = 5
    try:
        place_length = len(str(max(equal_list)))
    except:
        place_length = max(len(word) for word in equal_list)
    # place_length = len(str(max(col for row in init_list_of_list for col in row)))
    # print(place_length)
    if (a // y) == x:
        new_list_count = a//x
        count = -1
    else:
        raise ValueError("Factors of equal_list is not the dimensions of init_list_of_list ")
    # this means that the init_list_of_list dimensions are factorable and 1 to 1 to the equal_list
    for j, i in enumerate(equal_list):
        if (j % new_list_count) == 0:
            count += 1
        # init_list_of_list[count][(j % new_list_count)] = str(i).zfill(place_length)
        init_list_of_list[count][(j % new_list_count)] =  pad(str(i), place_length)
    return init_list_of_list

def example():
    # a factors of the length of equal_list must be init_display
    init_display = fill_in_list(50, 10)

    equal_list = []
    for i in range(500):
        if math.sqrt(i).is_integer():
            equal_list.append(i)
        else:
            equal_list.append(0)

    for_display = draw(init_display, equal_list)
    display(for_display)
    return 1

example()