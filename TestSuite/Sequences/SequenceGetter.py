################################################################################
# This file contains functions that return the sequences used in the test suite.
################################################################################

# The following functions return the sequences used in the test suite.
# The sequences are stored in text files in the TestSuite/Sequences folder.
# The functions read the sequences from the text files and return them as lists.
# The functions are used in the test suite to evaluate randomness.
    
def getModuloPrimeSpaceSequences():
    with open ("TestSuite/Sequences/mpsSequences.txt", "r") as f:
        sequence = []
        for line in f:
            sequence.append(line.replace("\n", "").replace("\t", ""))
        return sequence

def getLinearPolynomialSpaceSequences():
    with open ("TestSuite/Sequences/lpsSequences.txt", "r") as f:
        sequence = []
        for line in f:
            sequence.append(line.replace("\n", "").replace("\t", ""))
        return sequence

def getLFSRSequence_N10000_M14():
    with open ("TestSuite/Sequences/lfsrSequencesN=10000M=14.txt", "r") as f:
        sequences = []
        for line in f:
            sequences.append(line.replace("\n", "").replace("\t", ""))
        return sequences

def getLFSRSequence_N10000_M19():
    with open ("TestSuite/Sequences/lfsrSequencesN=10000M=19.txt", "r") as f:
        sequences = []
        for line in f:
            sequences.append(line.replace("\n", "").replace("\t", ""))
        return sequences

def getLFSRSequence_N10000_M29():
    with open ("TestSuite/Sequences/lfsrSequencesN=10000M=29.txt", "r") as f:
        sequences = []
        for line in f:
            sequences.append(line.replace("\n", "").replace("\t", ""))
        return sequences
    
def getTrulyRandomSeed_101():
    with open ("TestSuite/Sequences/true_random_seeds_101.txt", "r") as f:
        true_random_sequence_seeds = [int(line) for line in f]
        return true_random_sequence_seeds

def getTrulyRandomBits():
    with open ("TestSuite/Sequences/true_random.txt", "r") as f:
        true_random_sequence_bits = [int(line) for line in f]
        return true_random_sequence_bits