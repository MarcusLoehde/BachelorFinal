import matplotlib.pyplot as plt

def generate(a, b, p, x):
    """
    Generates an integer using the formula:
    (ax + b) mod p
    Args:
    a : int 
        The first seed in [0, p-1]
    b : int 
        The second seed in [0, p-1]
    p : int
        A prime number
    x : int 
        The constant value in [0, p-1]
    Returns:
    result : int 
        A pseudo-random integer
    """
    result = (a * x + b) % p
    return result

# Function to generate a sequence of integers
# n is the length of the sequence
def generate_bit_sequence(a, b, p):
    """
    Generates a bit sequence.
    Args:
    a : int 
        The first seed in [0, p-1]
    b : int
        The second seed in [0, p-1]
    p : int
        A prime number
    Returns:
    sequence : list
        A pseudo-random list of 0s and 1s
    """
    sequence = []
    for i in range(p):
        sequence.append(generate(a, b, p, i) % 2)
    return sequence

a = int(input("Enter a seed: "))
b = int(input("Enter another seed: "))
p = int(input("Enter a prime number: "))

print(f"Bit sequence:\n{generate_bit_sequence(a, b, p)}")

def generate_plot():
    """
    Generates a plot of the outputs by iterating x.
    """
    # Generate a plot of the outputs by iterating x
    a = 67
    b = 34
    p = 71
    results = {}
    for x in range(0, p-1):
       results[x] = generate(a, b, p, x)

    plt.plot(results.keys(), results.values(), 'ro')
    plt.title("All possible outputs with a=67, b=34")
    plt.xlabel("Value of x")
    plt.ylabel("Output of generator")

    plt.axis([0, p, 0, p])

    plt.show()

want_to_see_plot = input("Do you want to plot? (y/N): ")
if want_to_see_plot == "y":
    generate_plot()