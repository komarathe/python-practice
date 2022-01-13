#!/usr/bin/env python3

"""
File Name: collect_fq_seqs.py

Collect all the sequences from fastq file in a list.
"""

# Read fastq file in a read mode and create a file object
with open("sample.fq", "r") as fin:
    # Collect all the lines in the file handle in a list
    lines = fin.readlines()

# ----------------------------------------------------------------------
# Way 1
# Using for-loop

# Create an empty list to collect sequences
sequences_1 = []
for i in range(1, len(lines), 4):
    # Remove new line character from the sequence
    line = lines[i].strip()
    sequences_1.append(line)
print(sequences_1)
print("------")


# ---------------------------------------------------------------------
# Way 2
# Using while-loop

# Create an empty list to collect sequences
sequences_2 = []
i = 1
while i < len(lines):
    # Remove new line character from the sequence
    line = lines[i].strip()
    sequences_2.append(line)
    i += 4
print(sequences_2)


