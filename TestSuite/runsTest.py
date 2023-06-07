import numpy as np
from scipy.special import erfc
import Sequences.SequenceGetter as sg

def runs_test(sequence):
    """
    Perform the runs test on a given sequence.
    Args:
    sequence : str
        The bit string to be tested for randomness.
    Returns:
        p-value : float
    """
    n = len(sequence)

    # Compute the pre-test proportion π of ones in the input sequence
    pi = sequence.count('1') / n

    # Determine if the prerequisite Frequency test is passed
    tau = np.sqrt(2 / n)
    if abs(pi - 0.5) >= tau:
        return 0.0

    # Compute the test statistic v_n(obs)
    r = [0 if sequence[k] == sequence[k+1] else 1 for k in range(n-1)]
    v_n_obs = np.sum(r) + 1

    # Compute P-value
    p_value = erfc(abs(v_n_obs - 2.0 * n * pi * (1 - pi)) / (2.0 * np.sqrt(2 * n) * pi * (1 - pi)))

    return p_value

# Test the modulo prime space sequences
modulo_prime_sequence = sg.getModuloPrimeSpaceSequences()
results = []
for sequence in modulo_prime_sequence:
    P_value = runs_test(sequence)
    results.append(P_value >= 0.01)

print("Runs test for modulo prime sequences:")
print(f"Amount of passed tests: {sum(results)}")
print()

# Test the linear polynomial space sequences
linear_polynomial_sequence = sg.getLinearPolynomialSpaceSequences()
results = []
for sequence in linear_polynomial_sequence:
    P_value = runs_test(sequence)
    results.append(P_value >= 0.01)

print("Runs test for linear polynomial sequences:")
print(f"Amount of passed tests: {sum(results)}")
print()

# Test the LFSR sequences with N = 10000 and M = 14
lfsr_sequence = sg.getLFSRSequence_N10000_M14()
result = []
for sequence in lfsr_sequence:
    p_value = runs_test(sequence)
    result.append(p_value >= 0.01)

print("Runs test for LFSR sequences with N=10000 and M=14:")
print(f"Amount of passed tests: {sum(result)}")
print()

# Test the LFSR sequences with N = 10000 and M = 29
lfsr_sequence = sg.getLFSRSequence_N10000_M29()
result = []
for sequence in lfsr_sequence:
    p_value = runs_test(sequence)
    result.append(p_value >= 0.01)

print("Runs test for LFSR sequences with N=10000 and M=29:")
print(f"Amount of passed tests: {sum(result)}")
print()
