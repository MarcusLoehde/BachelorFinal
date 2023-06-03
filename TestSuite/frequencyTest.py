import numpy as np
import scipy.special as spc
import Sequences.SequenceGetter as sg

def frequency(sequence):
    """
    Perform the frequency test on a given sequence.
    Args:
    sequence : str
        The bit string to be tested for randomness.
    Returns:
        p-value : float
    """
    # Count the occurrence of zeroes and ones in the sequence
    n = len(sequence)
    count_1 = sequence.count("1")
    count_0 = n - count_1

    # Compute the test statistics
    s_obs = abs(count_1 - count_0) / np.sqrt(n)

    # Compute the P-value
    p_value = spc.erfc(s_obs / np.sqrt(2))

    return p_value

# Test the modulo prime space sequences
modulo_prime_sequence = sg.getModuloPrimeSpaceSequences()
results = []
for sequence in modulo_prime_sequence:
    p_value = frequency(sequence)
    results.append(p_value >= 0.01)

print("Frequency test for modulo prime sequences:")
print(f"Amount of sequences that pass the test: {sum(results)}")
print()

# Test the linear polynomial space sequences
linear_polynomial_sequence = sg.getLinearPolynomialSpaceSequences()
results = []
for sequence in linear_polynomial_sequence:
    p_value = frequency(sequence)
    results.append(p_value >= 0.01)

print("Frequency test for linear polynomial sequences:")
print(f"Amount of sequences that pass the test: {sum(results)}")
print()

# Test the LFSR sequences with n = 10000 and m = 14
lfsr_sequence = sg.getLFSRSequence_N10000_M14()
results = []
for sequence in lfsr_sequence:
    p_value = frequency(sequence)
    results.append(p_value >= 0.01)

print("Frequency test for LFSR sequences with N = 10000 and M = 14:")
print(f"Amount of sequences that pass the test: {sum(results)}")
print()

# Test the LFSR sequences with n = 10000 and m = 19
lfsr_sequence = sg.getLFSRSequence_N10000_M19()
results = []
for sequence in lfsr_sequence:
    p_value = frequency(sequence)
    results.append(p_value >= 0.01)

print("Frequency test for LFSR sequences with N = 10000 and M = 19:")
print(f"Amount of sequences that pass the test: {sum(results)}")
print()