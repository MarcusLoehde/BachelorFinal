import numpy as np
from scipy.fftpack import fft
from scipy.special import erfc
import Sequences.SequenceGetter as sg

def discrete_fourier_transform_test(sequence):
    """
    Perform the discrete Fourier transform test on a given sequence.
    Args:
    sequence : str
        The bit string to be tested for randomness.
    Returns:
        p-value : float
    """
    # Convert the binary sequence to +/- 1
    X = [1 if bit == '1' else -1 for bit in sequence]
    
    # Apply Discrete Fourier Transform
    S = fft(X)
    
    # Calculate M and T
    M = abs(S[:len(S)//2])
    T = np.sqrt(np.log(1/0.05)*len(X))
    
    # Compute N0 and N1
    n_0 = 0.95 * len(X) / 2
    n_1 = np.sum(M < T)
    
    # Compute d and P-value
    d = (n_1 - n_0) / np.sqrt(len(X) * 0.95 * 0.05 / 4)
    p_value = erfc(abs(d) / np.sqrt(2))

    return p_value

# Test the modulo prime space sequences
# modulo_prime_sequence = sg.getModuloPrimeSpaceSequences()
# result = []
# for sequence in modulo_prime_sequence:
#     p_value = discrete_fourier_transform_test(sequence)
#     result.append(p_value >= 0.01)

# print("Discrete Fourier Transform test for modulo prime space sequences:")
# print(f"Amount of passed tests: {sum(result)}")
# print()

# # Test the linear polynomial space sequences
# linear_polynomial_sequence = sg.getLinearPolynomialSpaceSequences()
# result = []
# for sequence in linear_polynomial_sequence:
#     p_value = discrete_fourier_transform_test(sequence)
#     result.append(p_value >= 0.01)

# print("Discrete Fourier Transform test for linear polynomial space sequences:")
# print(f"Amount of passed tests: {sum(result)}")
# print()

# # Test the LFSR sequences with N=10000 and M=14
# lfsr_sequence = sg.getLFSRSequence_N10000_M14()
# result = []
# for sequence in lfsr_sequence:
#     p_value = discrete_fourier_transform_test(sequence)
#     result.append(p_value >= 0.01)

# print("Discrete Fourier Transform test for LFSR sequences with N=10000 and M=14:")
# print(f"Amount of passed tests: {sum(result)}")
# print()

# # Test the LFSR sequences with N=10000 and M=19
# lfsr_sequence = sg.getLFSRSequence_N10000_M19()
# result = []
# for sequence in lfsr_sequence:
#     p_value = discrete_fourier_transform_test(sequence)
#     result.append(p_value >= 0.01)

# print("Discrete Fourier Transform test for LFSR sequences with N=10000 and M=19:")
# print(f"Amount of passed tests: {sum(result)}")
# print()

# Test the LFSR sequences with N=10000 and M=29
lfsr_sequence = sg.getLFSRSequence_N10000_M29()
result = []
for sequence in lfsr_sequence:
    p_value = discrete_fourier_transform_test(sequence)
    result.append(p_value >= 0.01)

print("Discrete Fourier Transform test for LFSR sequences with N=10000 and M=29:")
print(f"Amount of passed tests: {sum(result)}")
print()



