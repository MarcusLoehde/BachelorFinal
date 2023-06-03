import numpy as np
import Sequences.SequenceGetter as sg

def parity_function_test(sequence, m):
    """
    Perform the parity function test on a given sequence on all m blocks.
    Args:
    sequence : str
        The bit string to be tested for fooling the parity function.
    m : int
        The number of variables to be independent.
    Returns:
        result : int
    """
    # Create a list of parities
    parities = []
    for i in range(len(sequence) - m + 1):
        # extract m bits
        bits = sequence[i:i+m]
        # calculate parity
        parity = bits.count('1') % 2
        parities.append(parity)
    return parities

# Test the modulo prime sequence with N=10000
modulo_prime_sequence = sg.getModuloPrimeSpaceSequences()
result = 0
for sequence in modulo_prime_sequence:
    result += sum(parity_function_test(sequence, 2))
ratio = result / (len(modulo_prime_sequence) * 9999)

print("Parity function test for modulo prime space sequences:")
print(f"Amount of ones: {result}")
print(f"Ratio:  {ratio}")
print()

# Test the linear polynomial sequence with N=10000
linear_polynomial_sequence = sg.getLinearPolynomialSpaceSequences()
result = 0
for sequence in linear_polynomial_sequence:
    result += sum(parity_function_test(sequence, 2))
ratio = result / (len(linear_polynomial_sequence) * 9999)

print("Parity function test for linear polynomial space sequences:")
print(f"Amount of ones: {result}")
print(f"Ratio:  {ratio}")
print()

# Test the LFSR sequence with N=10000 and M=14
lfsr_sequence = sg.getLFSRSequence_N10000_M14()
result = 0
for sequence in lfsr_sequence:
    result += sum(parity_function_test(sequence, 14))
ratio = result / (len(lfsr_sequence) * 9987)

print("Parity function test for LFSR sequence with N=10000 and M=14:")
print(f"Amount of ones: {result}")
print(f"Ratio:  {ratio}")
print()

# Test the LFSR sequence with N=10000 and M=19
lfsr_sequence = sg.getLFSRSequence_N10000_M19()
result = 0
for sequence in lfsr_sequence:
    result += sum(parity_function_test(sequence, 19))
ratio = result / (len(lfsr_sequence) * 9982)

print("Parity function test for LFSR sequence with N=10000 and M=19:")
print(f"Amount of ones: {result}")
print(f"Ratio:  {ratio}")
print()