import ctools
def main():
    terminal_output = ctools.wopen("day7.d").split("\n")
    # print(terminal_output)
    # windows path: /\abc\jesus
    def accumilation(iterable, func=lambda x, y: x + "/" + y):
        iterator = iter(iterable)
        accumulated_value = next(iterator)
        yield accumulated_value

        for item in iterator:
            accumulated_value = func(accumulated_value, item)
            yield accumulated_value
    cwd = []
    sizes = {}
    for line in terminal_output:
        parts = line.strip().split(" ")
        if line[:4] == "$ cd":
            if parts[2] != "..":
                cwd.append(parts[2])
                gath = "/".join(cwd)
                sizes[gath] = 0
            else:
                cwd.pop()
        else:
            if parts[0].isnumeric():
                file_size = int(parts[0])
                for path in accumilation(cwd):
                    sizes[path] += file_size 
        print(cwd)
    total = 0
    for keys in sizes:
        if sizes[keys] < 100000:
            total += sizes[keys]
    print(total)

    must_free = sizes["/"] - 40000000 
    candidates = {}
    size_battle = []
    for keys in sizes:
        if sizes[keys] >= must_free:
            directory_and_size = (sizes[keys], keys)
            candidates[sizes[keys]] = keys
            size_battle.append(sizes[keys])

    least = sorted(size_battle)[0]
    print(least)
    print("Success")




























test_data = """$ cd /
$ ls
dir abc
12142 ppp
dir p
$ cd abc
$ ls
dir ggg
$ cd ggg
$ ls
87858 asdfw
$ cd ..
$ cd ..
$ cd p
$ ls
1234 z
"""
def test():
    # 
    data = test_data.strip().split("\n$")[1:]
    # print(data)
    # GET ALL DIRECTORY PATHS AND ATTACH TO THE FILES WITHIN IT
    cwd = ["/"]
    directory_tree = {}
    for line in data:
        # when ls grab all of the corresponding files.
        line = line.strip()
        if line[:2] == "ls":
            items = [tuple(i.split(" ")) for i in line[2:].strip().split("\n")]
            name = "/".join(cwd)
            directory_tree[name] = items
        elif line[:2] == "cd":
            parts = line.split(" ")
            if parts[1] == "..":
                cwd.pop()
            else:
                cwd.append(parts[1])
    # print(directory_tree)
    directory_size_beta = {}
    for key in directory_tree:
        files = directory_tree[key]
        # print(files, key)
        size_and_directories = []
        for file in files:
            # print(file[0])
            if file[0] == "dir":
                # print("dir")
                path = f'{key}/{file[1]}'
                size_and_directories.append(path)
            else:
                # print("int")
                size_and_directories.append(int(file[0]))
        directory_size_beta[key] = size_and_directories
    print(directory_size_beta)
    # directory is abspath/path :ex. //abc or //abc/asdf
    def find_directory_total(total, directory):
        try:
            total += sum(directory)
            return total
        except:
            return False


    print("Success")











# day7.py README.md log for the owner of this following code #

from collections import defaultdict
from itertools import accumulate

def sol(part):
    sizes = defaultdict(int)
    cwd = []

    with open("day7.d") as file:
        for line in file:
            items = line.split()
            if line.strip() == "$ cd ..":
                cwd.pop()
            elif line.startswith("$ cd"):
                cwd.append(items[-1])
            elif items[0].isnumeric():
                # when the first part of items is a number then add it to every path before it.
                for path in accumulate(cwd, func=lambda a, b: a + "/" + b):
                    # print(path)
                    sizes[path] += int(items[0])
                    # print(sizes[path])

    return sum(size for size in sizes.values() if size <= 100000) if part == 1 else min(size for size in sizes.values() if size >= sizes["/"] - 40000000)

if __name__ == "__main__":
    main()
    # test()  
    print(sol(1), sol(2))
