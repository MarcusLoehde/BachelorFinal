from pyfinite import ffield
import matplotlib.pyplot as plt

def generate(field : ffield.FField, n, x, y):
    """
    Generates a binary sequence.
    Args:
    field : FField
        A finite field
    n : int
        The length of the sequence
    x : int
        The first seed in [0, 2^m-1] (field size)
    y : int
        The second seed in [0, 2^m-1] (field size)
    Returns:
        result : list
    """
    m = field.n
    powers_of_x = [1]  # x^0 = 1
    for i in range(1, n):
        power = field.Multiply(powers_of_x[-1], x)
        powers_of_x.append(power)

    r = []
    y_coefficients = field.ShowCoefficients(y)
    for i in range(n):
        inner_product = 0
        powers_of_x_coefficients = field.ShowCoefficients(powers_of_x[i])
        for j in range(m + 1): # m + 1 because ffield adds one more index to the length of the coefficients
            inner_product = field.Add(inner_product, field.Multiply(powers_of_x_coefficients[j], y_coefficients[j]))
        r.append(inner_product)

    return r

m = int(input("Enter m as integer for the seed length: "))
field = ffield.FField(m)
n = int(input("Enter n as integer, used for the length of the sequence: "))
x = int(input(f"Enter seed x as integer between 0 and 2^{m}-1 ({2**m - 1}): "))
y = int(input(f"Enter seed y as integer between 0 and 2^{m}-1 ({2**m - 1}): "))

print(f"Sequence:\n{generate(field, n, x, y)}")

def generate_sequences_by_all_possible_seeds(output_size, seed_size):
    field = ffield.FField(seed_size)
    results = []
    highest = 2**seed_size
    for x in range(highest):
        for y in range(highest):
            result = generate(field, output_size, x, y)
            num = int("".join(str(i) for i in result), 2)
            results.append(num)
    
    return results

def count_occurences(results):
    # Count how many times each number appears
    counts = {}
    for result in results:
        if result in counts:
            counts[result] += 1
        else:
            counts[result] = 1

    return counts

def generate_plot_n8_m4():

    results = generate_sequences_by_all_possible_seeds(8, 4)
    counts = count_occurences(results)

    # Plot the counts of each number and label the axis and title
    plt.figure(figsize=(16, 6))  # Increase the figure width
    plt.bar(counts.keys(), counts.values(), color='royalblue', width=0.5)  # Change the color and width of the bars

    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal gridlines with reduced opacity
    plt.xlabel("Number", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.title(f"Count of each number for n={n}, epsilon=0.5", fontsize=16)

    plt.xticks(fontsize=12)  # Increase the font size of the x-axis ticks
    plt.yticks(fontsize=12)  # Increase the font size of the y-axis ticks

    plt.xlim(-10, 260)  # Set the limits of the x-axis
    plt.ylim(0, 80)  # Set the limits of the y-axis

    plt.show()

def generate_plot_n12_m8():
    results = generate_sequences_by_all_possible_seeds(12, 8)
    counts = count_occurences(results)

    # Plot the counts of each number and label the axis and title
    plt.figure(figsize=(16, 6))  # Increase the figure width
    plt.bar(counts.keys(), counts.values(), color='royalblue', width=2)  # Change the color and width of the bars

    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal gridlines with reduced opacity
    plt.xlabel("Number", fontsize=14)
    plt.ylabel("Count", fontsize=14)
    plt.title(f"Count of each number for n={n}, epsilon=3/64", fontsize=16)

    plt.xticks(fontsize=12)  # Increase the font size of the x-axis ticks
    plt.yticks(fontsize=12)  # Increase the font size of the y-axis ticks

    plt.xlim(-10, 4096)  # Set the limits of the x-axis
    plt.ylim(0, 900)  # Set the limits of the y-axis

    plt.show()

def calculate_almost_k_wise_independence():
    # Find all combinations of indices of size 8 on a sequence of length 12
    from itertools import combinations
    indices = list(combinations(range(12), 8))
    sequences = generate_sequences_by_all_possible_seeds(12, 8)

    # Iterate through all sequences and save the occurence in all the indices in some collection
    occurences = {}
    for sequence in sequences:
        sequence_bin = bin(sequence)[2:].zfill(12)
        for index in indices:
            key = ""
            for i in index:
                key += sequence_bin[i]
            if key in occurences:
                occurences[key] += 1
            else:
                occurences[key] = 1

def is_almost_k_wise_independent():
    import itertools
    from collections import Counter

    # Let's say this is your list of 4000 binary strings
    sequences = generate_sequences_by_all_possible_seeds(12, 8)

    # Create a counter to hold the counts of each 8-bit number
    counter = Counter()

    # Generate all combinations of 8 indices
    index_combinations = list(itertools.combinations(range(12), 8))

    # Iterate over each 12-bit binary string
    for number in sequences:
        binary_string = bin(number)[2:].zfill(12)
        # For each combination of indices, get the corresponding bits
        for index_combination in index_combinations:
            bit_combination = [binary_string[i] for i in index_combination]
            bit_combination_string = ''.join(bit_combination)

            # Combine the index combination and bit combination into a tuple
            combination = (index_combination, bit_combination_string)

            # Increment the count for this combination
            counter[combination] += 1

    # Now you can find the combination with the highest count
    most_common_combination = counter.most_common(1)

    print('The combination with the highest count is:', most_common_combination)


is_almost_k_wise_independent()

want_to_plot = input("Do you want to plot with n = 8 and m = 4? (y/N): ")
if want_to_plot == "y":
    generate_plot_n8_m4()

want_to_plot = input("Do you want to plot with n = 12 and m = 8? (y/N): ")
if want_to_plot == "y":
    generate_plot_n12_m8()

