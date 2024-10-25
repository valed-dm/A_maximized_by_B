# Function to return the maximized value of A
# https://www.geeksforgeeks.org/maximize-the-value-of-a-by-replacing-some-of-its-digits-with-digits-of-b/

def max_value(str_a: str, str_b: str) -> str:
    # Sort B's digits in descending order
    sorted_b = sorted(str_b, reverse=True)

    # Replace characters in A only if there are remaining larger digits in sorted B
    result = []
    j = 0  # Track the position in sorted_b

    for char in str_a:
        # Replace if the current digit in sorted_b is larger
        if j < len(sorted_b) and sorted_b[j] > char:
            result.append(sorted_b[j])
            j += 1
        else:
            result.append(char)

    return ''.join(result)


# Data
a = "1234"
b = "4321"

print(repr(max_value(a, b)))
