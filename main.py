# Function to return the maximized value of A

def max_value(str_a: str, str_b: str) -> str:
    # Sort digits in ascending order
    str_b = sorted(str_b)
    print(str_b)
    bi = [i for i in str_b]
    print(bi)
    ai = [i for i in str_a]
    print(ai)

    n = len(str_a)
    m = len(str_b)

    # j points to largest digit in B
    j = m - 1
    for i in range(n):

        # If all the digits of b
        # have been used
        if j < 0:
            break

        if bi[j] > ai[i]:
            ai[i] = bi[j]

            # Current digit has been used
            j -= 1

    # Return the maximized value
    x = "".join(ai)
    return x


# Data
a = "1434"
b = "437108"

print(repr(max_value(a, b)))
