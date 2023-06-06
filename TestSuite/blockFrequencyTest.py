import numpy as np
from scipy.special import gammaincc
import Sequences.SequenceGetter as sg

def block_frequency_test(sequence, m):
    """
    Perform the block frequency test on a given sequence.
    Args:
    sequence : str
        The bit string to be tested for randomness.
    m : int
        The length of each block.
    Returns:
        p-value : float
    """
    n = len(sequence)
    N = n // m

    # Discard unused bits
    sequence = sequence[:N*m]
    
    # Partition the input sequence into N non-overlapping blocks
    blocks = np.array([sequence[i:i+m] for i in range(0, len(sequence), m)])

    # Determine the proportion of ones in each M-bit block
    pi = np.array([block.count('1') / m for block in blocks])

    # Compute the chi-square statistic
    chi_squared_obs = 4 * m * np.sum((pi - 0.5) ** 2)

    # Compute P-value
    p_value = gammaincc(N/2, chi_squared_obs/2)
    
    return p_value


# Test the modulo prime space sequences
modulo_prime_sequence = sg.getModuloPrimeSpaceSequences()
results = {}
for sequence in modulo_prime_sequence:
    for m in range(200, 1001, 100):
        P_value = block_frequency_test(sequence, m)
        if m not in results:
            results[m] = []
        results[m].append(P_value >= 0.01)
    
print("Block frequency test for modulo prime sequences:")
for m in results:
    print(f"M = {m}: {sum(results[m])}")
print()


# Test the linear polynomial space sequences
linear_polynomial_sequence = sg.getLinearPolynomialSpaceSequences()
results = {}
for sequence in linear_polynomial_sequence:
    for m in range(200, 1001, 100):
        P_value = block_frequency_test(sequence, m)
        if m not in results:
            results[m] = []
        results[m].append(P_value >= 0.01)

print("Block frequency test for linear polynomial sequences:")
for m in results:
    print(f"M = {m}: {sum(results[m])}")
print()

# Test the LFSR sequences with N = 10000 and M = 14
lfsr_sequence = sg.getLFSRSequence_N10000_M14()
results = {}
for sequence in lfsr_sequence:
    for m in range(200, 1001, 100):
        P_value = block_frequency_test(sequence, m)
        if m not in results:
            results[m] = []
        results[m].append(P_value >= 0.01)

print("Block frequency test for LFSR sequences with N = 10000 and M = 14:")
for m in results:
    print(f"M = {m}: {sum(results[m])}")
print()

# Test the LFSR sequences with N = 10000 and M = 19
lfsr_sequence = sg.getLFSRSequence_N10000_M19()
results = {}
for sequence in lfsr_sequence:
    for m in range(200, 1001, 100):
        P_value = block_frequency_test(sequence, m)
        if m not in results:
            results[m] = []
        results[m].append(P_value >= 0.01)

print("Block frequency test for LFSR sequences with N = 10000 and M = 19:")
for m in results:
    print(f"M = {m}: {sum(results[m])}")
print()

# Test the LFSR sequences with N = 10000 and M = 29
lfsr_sequence = sg.getLFSRSequence_N10000_M29()
results = {}
for sequence in lfsr_sequence:
    for m in range(200, 1001, 100):
        P_value = block_frequency_test(sequence, m)
        if m not in results:
            results[m] = []
        results[m].append(P_value >= 0.01)
    
print("Block frequency test for LFSR sequences with N = 10000 and M = 29:")
for m in results:
    print(f"M = {m}: {sum(results[m])}")
print()