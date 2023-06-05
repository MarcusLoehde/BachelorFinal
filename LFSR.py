from pyfinite import ffield
import numpy as np
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
        A pseudo-random list of 0s and 1s
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
    """
    Generates all possible sequences for a given output size and seed size.
    Args:
    output_size : int
        The length of the output sequence
    seed_size : int
        The length of the seeds
    Returns:
    results : list
        A list of all possible pseudo-random sequences
    """
    field = ffield.FField(seed_size)
    results = []
    highest = 2**seed_size
    for x in range(highest):
        for y in range(highest):
            result = generate(field, output_size, x, y)
            #num = int("".join(str(i) for i in result), 2)
            results.append(result)
    
    return results

def count_occurences(results):
    """
    Counts the occurences of each number in a list.
    Args:
    results : list
        A list of pseudo-random sequences
    Returns:
    counts : dict
        A dictionary of the counts of each number
    """
    # Count how many times each number appears
    counts = {}
    for result in results:
        num = int("".join(str(i) for i in result), 2)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return counts

def generate_plot_n8_m4():
    """
    Generates a plot of the counts of each number for n=8 and m=4.
    """
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
    """
    Generates a plot of the counts of each number for n=12 and m=8.
    """
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

def is_almost_k_wise_independent(n, m):
    """
    Checks if the sequences of length n is almost k-wise independent, and prints the result.
    Args:
    n : int
        The length of the sequences
    m : int
        The length of the seeds
    """
    import itertools
    from collections import Counter

    # Let's say this is your list of 4000 binary strings
    sequences = generate_sequences_by_all_possible_seeds(n, m)

    # Create a counter to hold the counts of each 8-bit number
    counter = Counter()

    # Generate all combinations of 8 indices
    index_combinations = list(itertools.combinations(range(n), m))

    # Iterate over each 12-bit binary string
    for sequence in sequences:
        # For each combination of indices, get the corresponding bits
        for index_combination in index_combinations:
            bit_combination = [sequence[i] for i in index_combination]
            bit_combination_string = "".join(str(i) for i in bit_combination)

            # Combine the index combination and bit combination into a tuple
            combination = (index_combination, bit_combination_string)

            # Increment the count for this combination
            counter[combination] += 1

    # Now we can find the combination with the highest count
    most_common_combination = counter.most_common(1)
    print('The combination with the highest count is:', most_common_combination)

    # Check if the sequence is almost m-wise independent by calculating the probabilities
    eps = n/(2**m)
    prob_most_common_combination = most_common_combination[0][1]/(len(sequences))
    prob_difference = np.abs(prob_most_common_combination - 2**(-m))

    # Print the result defined by the upper bound of epsilon
    result = prob_difference <= eps
    print(f"Is the sequence almost {m}-wise independent? {result}")


check_almost_kwise_independence_n8_m4 = input("Do you want to check for almost 4-wise independence with n = 8 and m = 4? (y/N): ")
if check_almost_kwise_independence_n8_m4 == "y":
    is_almost_k_wise_independent(8, 4)

check_almost_kwise_independence_n12_m8 = input("Do you want to check for almost 8-wise independence with n = 12 and m = 8? (y/N): ")
if check_almost_kwise_independence_n12_m8 == "y":
    is_almost_k_wise_independent(12, 8)

want_to_plot = input("Do you want to plot with n = 8 and m = 4? (y/N): ")
if want_to_plot == "y":
    generate_plot_n8_m4()

want_to_plot = input("Do you want to plot with n = 12 and m = 8? (y/N): ")
if want_to_plot == "y":
    generate_plot_n12_m8()

