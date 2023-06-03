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
        for j in range(m):
            #inner_product = field.Add(inner_product, field.Multiply(powers_of_x_coefficients[j], y_coefficients[-j - 1]))
            inner_product = field.Add(inner_product, field.Multiply(powers_of_x_coefficients[j], y_coefficients[j]))
        r.append(inner_product)

    return r

m = int(input("Enter m as integer for the seed length: "))
field = ffield.FField(m)
n = int(input("Enter n as integer, used for the length of the sequence: "))
x = int(input(f"Enter seed x as integer between 0 and 2^{m}-1 ({2**m - 1}): "))
y = int(input(f"Enter seed y as integer between 0 and 2^{m}-1 ({2**m - 1}): "))

print(f"Sequence:\n{generate(field, n, x, y)}")

field = ffield.FField(4)
n = 8
x = 13
y = 4
print(generate(field, n, x, y))

# # Define the finite field
# field = ffield.FField(19)

# # Example usage:
# n = 10000
# x_seeds = []
# y_seeds = []
# with open("TestSuite/Sequences/trulyRandomSeedsLen=19", "r") as f:
#     for i in range(10000):
#         x_seeds.append(int(f.readline().strip()))
#         y_seeds.append(int(f.readline().strip()))

# start_time = time.time()
# results = []
# for i in range(10000):
#     results.append(generate_num(field, n, x_seeds[i], y_seeds[i]))
#     print(i)

# end_time = time.time()

# with open("TestSuite/Sequences/lfsrSequenceN=10000M=19.txt", "w") as f:
#     for i in results:
#         f.write(str(i).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""))
#         f.write("\n")

# print(f"Time to generate all possible combinations of x and y: {end_time - start_time} seconds")


# Generate all possible combinations of x and y 
field = ffield.FField(4)
n = 8

results = []
for x in range(16):
    for y in range(16):
        result = generate(field, n, x, y)
        num = int("".join(str(i) for i in result), 2)
        results.append(num)

# Count how many times each number appears where we convert the bitstrings to ints
counts = {}
for result in results:
    if result in counts:
        counts[result] += 1
    else:
        counts[result] = 1

# Print the largest and smallest counts
print("Largest counts:")

#for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:10]:
#    print(f"{key}: {value}")
#    print(f"{key}, {counts[key]}")
#print("Smallest counts:")
#for key, value in sorted(counts.items(), key=lambda item: item[1])[:10]:
#    print(f"{key}: {value}")
#    print(f"{key}, {counts[key]}")


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

# Calculate the probability of each number
total = sum(counts.values())
probabilities = {}
for key, value in counts.items():
    probabilities[key] = value / total

# Print the largets and smallest probabilities
print("Largest probabilities:")
for key, value in sorted(probabilities.items(), key=lambda item: item[1], reverse=True)[:1]:
    print(f"{key}: {value}")
    print(f"{key}, {counts[key]}")
print("Smallest probabilities:")
for key, value in sorted(probabilities.items(), key=lambda item: item[1])[:1]:
    print(f"{key}: {value}")
    print(f"{key}, {counts[key]}")
