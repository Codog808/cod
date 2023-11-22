def babylonian_sqrt(number, iterations=9):
    old_guess = number/2
    half = 1/2
    for _ in range(iterations):
        old_guess = half*(old_guess + number/old_guess)
    return old_guess

def main():
    for i in range(3):
        print(babylonian_sqrt(3, i))

if __name__ == "__main__":
    main()
