def calculate_pi_chudnovsky(num_terms):
    """
    Calculate an approximation of Pi using the Chudnovsky algorithm.
    
    The Chudnovsky algorithm is a fast method for calculating the digits of Pi,
    based on Ramanujan-type formulas. It involves complex calculations including
    factorials, and each term in the series adds many correct digits to the approximation.
    
    Args:
    num_terms (int): The number of terms to use in the series. More terms increase accuracy.

    Returns:
    float: An approximation of Pi.
    """

    from decimal import Decimal, getcontext
    import math

    # Setting the precision for Decimal calculations
    # Precision is set higher than the number of digits to ensure accuracy
    getcontext().prec = num_terms + 5

    # The constant factor in the Chudnovsky formula
    C = 426880 * Decimal(10005).sqrt()

    # The summation part of the Chudnovsky formula
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, num_terms):
        M = (M * (K ** 3 - 16 * K)) // i ** 3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    # Calculating pi using the Chudnovsky formula
    pi = C / S

    # Returning pi with the set precision
    return +pi

# Example usage: Calculate Pi using 5 terms of the Chudnovsky algorithm
pi_approximation = calculate_pi_chudnovsky(5)
print(pi_approximation)

