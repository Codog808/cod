import time

def current_value(x):
    print(f"Current Value: {x}")
    return 0

def main(iterator):
    to_file = []
    for x in range(iterator):
        time.sleep(1)
        val = x**2
        current_value(str(val) + f" | Index Value: {x}")
        to_file.append(str(val))

    with open("t", "w") as f:
        f.write("\n".join(to_file))
        f.close()
    print("operation done")

main(1_000)
