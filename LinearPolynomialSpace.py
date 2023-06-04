from pyfinite import ffield
import matplotlib.pyplot as plt
import numpy as np

def generate(a, b, field, x):
    """
    Generates a binary sequence using the formula:
    ax + b
    Args:
    a : int
        The first seed in [0, 2^n-1] (field size)
    b : int
        The second seed in [0, 2^n-1] (field size)
    field : FField
        A finite field
    x : int
        The constant value in [0, 2^n-1] (field size)
    Returns:
        result : list
    """
    result = field.Add(field.DoMultiply(a, x), b)
    return field.ShowCoefficients(result)

def generate_bit_sequence(a, b, field):
    """
    Generates binary sequences.
    Args:
    a : int
        The first seed in [0, 2^n-1] (field size)
    b : int
        The second seed in [0, 2^n-1] (field size)
    field : FField
        A finite field
    Returns:
        result : list[list]
    """
    result = []
    for i in range(2**field.n):
        result.append(generate(a, b, field, i))
    return result


n = int(input("Enter n as integer, used for the field: "))
r = 2**n-1
a = int(input(f"Enter random a integer between 0 and 2^{n}-1 ({r}): "))
b = int(input(f"Enter random b integer between 0 and 2^{n}-1 ({r}): "))
field = ffield.FField(n)

# Generate a bit sequence
bit_sequence = generate_bit_sequence(a, b, field)
print(f"Bit sequence:\n{bit_sequence}")

def generate_plot():
    # Generate a plot of the outputs by iterating x

    def binary_to_integer(binary_array):
        # Convert the binary array into a string
        binary_string = ''.join(str(bit) for bit in binary_array)
        # Convert the binary string into a decimal integer
        decimal_int = int(binary_string, 2)
        return decimal_int

    a = 27
    b = 86
    field = ffield.FField(8)

    results = {}
    for x in range(0, 2**field.n-1):
        results[x] = binary_to_integer(generate(a, b, field, x))

    plt.plot(results.keys(), results.values(), 'bo')
    plt.grid(True)
    plt.xlim(0, 256)  # Set the limits of the x-axis
    plt.ylim(0, 256)  # Set the limits of the y-axis
    plt.title(f"All possible outputs with a={a}, b={b}")
    plt.xlabel("Value of x")
    plt.ylabel("Output of generator")
    plt.show()

want_to_plot = input("Do you want to plot? (y/N): ")
if want_to_plot == 'y':
    generate_plot()