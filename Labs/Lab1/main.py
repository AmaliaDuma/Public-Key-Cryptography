import time


def gcd1(a, b):
    """
    Finds the greatest common divisor of two numbers by continuously dividing the bigger number with the smaller one.\n
    :param a: 1st number
    :param b: 2nd number
    :return: Greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcd1(b, a % b)


def gcd2(a, b):
    """
    Finds the greatest common divisor by using the Euclidean algorithm by subtraction.\n
    :param a: 1st number
    :param b: 2nd number
    :return: Greatest common divisor of a and b
    """
    if a == 0:
        return b
    if b == 0:
        return a

    if a == b:
        return a

    if a > b:
        return gcd2(a-b, b)
    return gcd2(a, b-a)


def gcd3(a, b):
    """
    Find the greatest common divisor by getting the min of the two numbers, then finds the highest common factor of that min.\n
    :param a: 1st number
    :param b: 2nd number
    :return: Greatest common divisor of a and b
    """
    min_nr = min(a, b)

    while min_nr:
        if a % min_nr == 0 and b % min_nr == 0:
            break
        min_nr -= 1

    return min_nr


if __name__ == '__main__':
    tests = [
        (32, 264),
        (171, 2310),
        (3820, 15280),
        (712, 4),
        (255, 177),
        (10621, 3957201),
        (4137524, 1227244),
        (74, 41992),
        (2031978, 396324)
    ]

    for test in tests:
        x = test[0]
        y = test[1]
        print("\nx={},y={}".format(x, y))

        print("Start GCD -> 1.Dividing method")
        start = time.time()
        gcd = gcd1(x, y)
        end = time.time()
        print("Time elapsed: {} seconds".format(end - start))
        print("Gcd is {}\n".format(gcd))

        print("Start GCD -> 2.Subtracting method")
        start = time.time()
        gcd = gcd2(x, y)
        end = time.time()
        print("Time elapsed: {} seconds".format(end - start))
        print("Gcd is {}\n".format(gcd))

        print("Start GCD -> 3.Brute force method")
        start = time.time()
        gcd = gcd3(x, y)
        end = time.time()
        print("Time elapsed: {} seconds".format(end - start))
        print("Gcd is {}\n".format(gcd))
