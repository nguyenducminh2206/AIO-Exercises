def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def approx_sin(x, n):
    """
    Calculate approximate sin function.
    """
    result = 0

    for i in range(n):
        term = ((-1)**i * x**(2*i + 1) / factorial(2*i + 1))
        result += term
    return result


def approx_cos(x, n):
    """
    Calculate approximate cos function.
    """
    result = 0

    for i in range(n):
        term = ((-1)**i * x**(2*i) / factorial(2*i))
        result += term
    return result


def approx_sinh(x, n):
    """
    Calculate approximate sinh function.
    """
    result = 0

    for i in range(n):
        term = (x**(2*i + 1)) / factorial(2*i + 1)
        result += term
    return result


def approx_cosh(x, n):
    """
    Calculate approximate cosh function.
    """
    result = 0

    for i in range(n):
        term = (x**(2*i)) / factorial(2*i)
        result += term
    return result


def main():
    x = float(input('Input x (radians): '))
    n = int(input('Input number of terms: '))

    if n <= 0:
        print('n must be a positive integer')
        return

    # Question 10 (Multiple choice)
    print(f'aprrox_sin({x}, {n}): {approx_sin(x, n):.4f}')
    # Question 9 (Multiple choice)
    print(f'aprrox_cos({x}, {n}): {approx_cos(x, n):.2f}')
    # Question 11 (Multiple choice)
    print(f'aprrox_sinh({x}, {n}): {approx_sinh(x, n):.2f}')
    # Question 12 (Multiple choice)
    print(f'aprrox_cosh({x}, {n}): {approx_cosh(x, n):.2f}')


if __name__ == "__main__":
    main()
