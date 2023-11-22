from sys import exception


def wopen(filename):
    """ quick way to open files, I guess... """
    with open(filename) as f:
        return f.read()

def prnt(text):
    """ to display answers better, I guess """
    print(f"\n\n{text}\n\n")

class cmath:
    @classmethod
    def square_root(cls, n, iterations=9):
        x = n / 2
        for _ in range(iterations):
            x = 0.5 * (x + n / 2)
        return x
    @classmethod
    def absolute_value(cls, n):
        square = n * n
        root = cls.square_root(square)
        return root

def organize_files():
    import os
    from collections import defaultdict
    import shutil
    filenames = os.listdir()
    # file_parts = [i.split() for i in filenames]
    file_parts = [[i for i in file] for file in filenames]
    folders = defaultdict(list)
    for file in file_parts:
        day = []
        for part in file:
            print(part) 
            if part.isnumeric():
                day.append(part)
            print(day)
        if day:
            day_name = int("".join(day))
            folders[day_name].append("".join(file))
    print(folders)
    for key in folders:
        print(key)
        print(folders[key])
        try:
            os.mkdir(str(key))
            files = folders[key]
            for file in files:
                shutil.move(file, str(key))
        except exception as e:
            print("e" , e, key)

    

def main():
    """ to create the dayN python and data file """
    import sys
    day = sys.argv[1]
    if int(day):
        file_base = f"day{day}"
        init = f"""import ctools
def main():
    data = ctools.wopen("{file_base}.d")
    print("success")
if __name__ == "__main__":
    main()
        """
        with open(f"{file_base}.d", "w") as f:
            f.write("")
        with open(f"{file_base}.py", "w") as f:
            f.write(init)
        print("success")

if __name__ == "__main__":
    # main()
    # print(cmath.square_root(4))
    # print(cmath.absolute_value(-4))
    # print(cmath.absolute_value(4))
    organize_files()
