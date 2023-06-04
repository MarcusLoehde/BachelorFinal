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

def generate_sequences_by_all_possible_seeds(seed_size):
    field = ffield.FField(seed_size)
    results = []
    highest = 2**seed_size
    for x in range(highest):
        for y in range(highest):
            result = generate(field, n, x, y)
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
    # Generate all possible combinations of x and y 
    field = ffield.FField(4)
    n = 8

    results = generate_sequences_by_all_possible_seeds(4)
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
    # Generate all possible combinations of x and y 
    field = ffield.FField(8)
    n = 12

    results = generate_sequences_by_all_possible_seeds(8)
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


want_to_plot = input("Do you want to plot with n = 8 and m = 4? (y/N): ")
if want_to_plot == "y":
    generate_plot_n8_m4()

want_to_plot = input("Do you want to plot with n = 12 and m = 8? (y/N): ")
if want_to_plot == "y":
    generate_plot_n12_m8()

