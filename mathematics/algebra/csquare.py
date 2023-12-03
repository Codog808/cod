def babylonian_sqrt(n, attempts=9, tolerance=1e-10):
    guess = n / 2.0
    for _ in range(attempts):
        guess = 0.5 * (guess + n/guess)
    return guess

def binary_sqrt(n, attempts=9, tolerance=1e-10):
    low, high = 0, n
    guess = (low + high) / 2.0
    
    for _ in range(attempts):
        if guess**2 < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0

    return guess

def main():
    for i in range(3):
        print(babylonian_sqrt(3, i))

if __name__ == "__main__":
    main()
# def main():
#     print(binary_sqrt(64))
#     print(babylonian_sqrt(64))
#     print("success")

# if __name__ == '__main__':
#     main()
# def babylonian_sqrt(number, iterations=9):
#     old_guess = number/2
#     half = 1/2
#     for _ in range(iterations):
#         old_guess = half*(old_guess + number/old_guess)
#     return old_guess

