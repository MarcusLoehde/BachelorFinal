import Sequences.SequenceGetter as sg

def check_almost_kwise_independence(sequence, k, eps):
    """
    Check that for every combination of k-bit strings, the number of occurrences of the k-bit string is approximately the same.
    Args:
    sequence : str
        The bit string to be tested for independence.
    k : int
        The number of variables to be independent.
    eps : float
        The maximum allowed difference between the number of occurrences of the k-bit string.
    Returns:
        result : bool
    """
    # Create a dictionary to store the number of occurrences of each k-bit string
    k_bit_strings = {}
    # Loop over all k-bit strings
    for i in range(len(sequence) - k + 1):
        # extract k bits
        bits = sequence[i:i+k]
        # Check if the k-bit string is already in the dictionary
        if bits in k_bit_strings:
            # If it is, add one to the number of occurrences
            k_bit_strings[bits] += 1
        else:
            # If it is not, add the k-bit string to the dictionary
            k_bit_strings[bits] = 1
    # Calculate the uniform probability of occurrences of a k-bit string
    uniform_prob =  1 / (2 ** k)
    # Loop over all k-bit strings, calculate its probability of occurrences and compare it to the uniform probability
    for bit_string in k_bit_strings:
        # Check if the difference between the probability of occurrences and the uniform probability is larger than eps
        bit_string_prob = k_bit_strings[bit_string] / (len(sequence) - k + 1)
        if abs(bit_string_prob - uniform_prob) > eps:
            # If it is, return False
            return False
    # If all k-bit strings have approximately the same number of occurrences, return True
    return True

# # Test the LFSR sequence with N=10000 and M=14
# lfsr_sequence = sg.getLFSRSequence_N10000_M14()
# result = 0
# eps = 625/1024
# k = 9999
# for sequence in lfsr_sequence:
#     result += check_almost_kwise_independence(sequence, k, eps)

# print("Independence test for LFSR sequence with N=10000 and M=14:")
# print(f"Amount of sequences being {k}-wise independent: {result}")
# print()

# # Test the LFSR sequence with N=10000 and M=19
# lfsr_sequence = sg.getLFSRSequence_N10000_M19()
# result = 0
# eps = 625/32768
# k = 9948
# for sequence in lfsr_sequence:
#     result += check_almost_kwise_independence(sequence, k, eps)

# print("Independence test for LFSR sequence with N=10000 and M=19:")
# print(f"Amount of sequences being {k}-wise independent: {result}")
# print()

from itertools import combinations, product
import numpy as np

def check_independence(sequence, k, eps):
    n = len(sequence)
    
    # Generate all k-bit binary strings
    k_bit_strings = [''.join(map(str, bits)) for bits in product([0, 1], repeat=k)]
    
    # Check all combinations of k positions
    for positions in combinations(range(n), k):
        for k_bit_str in k_bit_strings:
            # Count occurrences of k_bit_str at the selected positions
            count = sum(sequence[i] == int(k_bit_str[j]) for i, j in zip(positions, range(k)))
            
            # Calculate the probability
            prob = count / 2**k
            
            # Check the condition for (eps, k)-independence
            if np.abs(prob - 2**-k) > eps:
                return False  # The sequence is not (eps, k)-independent
    
    # If we have not returned yet, the sequence is (eps, k)-independent
    return True

lfsr_sequence = sg.getLFSRSequence_N10000_M14()
k = 10
eps = 625/1024
result = 0
for sequence in lfsr_sequence:
    is_independent = check_independence(lfsr_sequence, k, eps)
    result += is_independent

print(f"The sequence is {'' if is_independent else 'not '}(ε, k)-independent.")


