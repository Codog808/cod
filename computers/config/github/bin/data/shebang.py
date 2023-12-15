#!/usr/bin/env python3
import os

def add_shebang(directory="."):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            with open(filename, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write("#!/usr/bin/env python3\n" + content)

if __name__ == "__main__":
    add_shebang()
