from math import sqrt, modf

def generalized_fermat(n, B):
    # For k = 1,2, ... do:
    k = 1
    while True:
        # Let t0 = [square_root(k*n)]
        t0 = modf(sqrt(k*n))[1]

        # For t = t0 + 1, ..., t0 + B do:
        t = t0 + 1
        while t <= t0 + B:
            # If (t^2 - k*n) is a square s^2 =>
            #          s^2 = t^2 - k*n, n = 1/k * (t - s) * (t + s) and stop
            # Else continue
            root = sqrt(t**2 - k*n)
            if int(root + 0.5) ** 2 == t**2 - k*n:
                s = sqrt(t*t - k*n)
                if (t-s) % k == 0:
                    return (t - s) / k, (t + s)
                else:
                    return (t - s), (t + s) / k
            t += 1
        k += 1


if __name__ == '__main__':
    result = generalized_fermat(37, 8)
    if result[0] == 1 or result[1] == 1:
        print("Nr is already prime")
    else:
        print(result)



