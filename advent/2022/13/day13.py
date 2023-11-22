def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]
    if isinstance(a, int) and isinstance(b, list):
        a = [a]
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a == b:
             return 0
        else:
             return -1
    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            x = compare(a[i], b[i])
            if x == 1:
                return 1
            if x == -1:
                return -1
            i += 1

        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1
        return -1

def part_1():
    """ 
    distress signal reorder 
    
    """
    with open("day13.d") as f:
        parts = f.read().strip().split("\n\n")

    ans = 0

    for i, packet in enumerate(parts):
        a, b = map(eval, packet.split("\n"))
        if compare(a, b) == 1:
            ans += i + 1
    print("Part 1 Success")
    return ans

def part_2():
    from functools import cmp_to_key
    with open("day13.d") as f:
        packets = f.read().strip().replace("\n\n", "\n").split("\n")
    lists = list(map(eval, packets))
    lists.append([[2]])
    lists.append([[6]])
    # key is how we sort the list
    lists = sorted(lists, key=cmp_to_key(compare), reverse=True)


    for i, li in enumerate(lists):
        if li == [[2]]:
            a = i + 1
        if li == [[6]]:
            b = i + 1
    print("part 2 successful")
    return (a * b)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
