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
    """
    sequence = []
    for i in range(p):
        sequence.append(generate(a, b, p, i) % 2)
    return sequence

a = int(input("Enter a seed: "))
b = int(input("Enter another seed: "))
p = int(input("Enter a prime number: "))

print(f"Bit sequence:\n{generate_bit_sequence(a, b, p)}")