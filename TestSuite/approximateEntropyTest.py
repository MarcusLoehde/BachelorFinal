from scipy.special import gammaincc
from collections import defaultdict
import numpy as np
import Sequences.SequenceGetter as sg

def approximate_entropy_test(sequence, m):    
    """
    Perform the approximate entropy test on a given sequence.
    Args:
    sequence : str
        The bit string to be tested for randomness.
    m : int
        The length of each block.
    Returns:
        p-value : float
    """
    n = len(sequence)

    def compute_phi_m(sequence, m):
        n = len(sequence)

        # Append the first m-1 bits of the sequence to the end of the sequence
        first_m_minus_1_bits = sequence[:m-1]
        sequence += first_m_minus_1_bits

        # Create a dictionary to store the frequencies of each m-bit pattern
        # Initialize the dictionary with all possible m-bit patterns
        frequency_count = defaultdict(int)
        for i in range(2**m):
            frequency_count[bin(i)[2:].zfill(m)] = 0
    
        for i in range(n):
            frequency_count[sequence[i:i+m]] += 1

        # Compute C_i^m for each value of i in the frequency count dictionary
        C_i_m = {}
        for key in frequency_count:
            C_i_m[key] = frequency_count[key] / n

        # Compute phi_m
        phi_m = 0
        for key in C_i_m:
            if C_i_m[key] != 0:
                phi_m += C_i_m[key] * np.log(C_i_m[key])
        
        return phi_m

    phi_m = compute_phi_m(sequence, m)
    phi_m_plus_1 = compute_phi_m(sequence, m+1)

    # Compute the test statistic
    ap_en = phi_m - phi_m_plus_1
    chi_2 = 2 * n * (np.log(2) - ap_en)

    # Compute the p-value
    p_value = gammaincc(2**(m-1), chi_2 / 2)

    return p_value

# Test the modulo prime space sequences
modulo_prime_sequence = sg.getModuloPrimeSpaceSequences()
results = {}
for sequence in modulo_prime_sequence:
    for m in range(2, 8):
        p_value = approximate_entropy_test(sequence, m)
        if m not in results:
            results[m] = 0
        results[m] += (p_value >= 0.01)

print("Approximate entropy test for modulo prime sequences:")
for m in range(2, 8):
    print(f"Amount of sequences that pass the test with m = {m}: {results[m]}")
print()

# Test the linear polynomial space sequences
linear_polynomial_sequence = sg.getLinearPolynomialSpaceSequences()
results = {}
for sequence in linear_polynomial_sequence:
    for m in range(2, 8):
        p_value = approximate_entropy_test(sequence, m)
        if m not in results:
            results[m] = 0
        results[m] += (p_value >= 0.01)

print("Approximate entropy test for linear polynomial sequences:")
for m in range(2, 8):
    print(f"Amount of sequences that pass the test with m = {m}: {results[m]}")
print()

# Test the LFSR sequence with N = 10000 and M = 14
lfsr_sequence = sg.getLFSRSequence_N10000_M14()
results = {}
for sequence in lfsr_sequence:
    for m in range(2, 8):
        p_value = approximate_entropy_test(sequence, m)
        if m not in results:
            results[m] = 0
        results[m] += (p_value >= 0.01)

print("Approximate entropy test for LFSR sequences with N = 10000 and M = 14:")
for m in range(2, 8):
    print(f"Amount of sequences that pass the test with m = {m}: {results[m]}")

# Test the LFSR sequence with N = 10000 and M = 19
lfsr_sequence = sg.getLFSRSequence_N10000_M19()
results = {}
for sequence in lfsr_sequence:
    for m in range(2, 8):
        p_value = approximate_entropy_test(sequence, m)
        if m not in results:
            results[m] = 0
        results[m] += (p_value >= 0.01)

print("Approximate entropy test for LFSR sequences with N = 10000 and M = 19:")
for m in range(2, 8):
    print(f"Amount of sequences that pass the test with m = {m}: {results[m]}")