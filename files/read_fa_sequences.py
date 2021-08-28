#!/usr/bin/env python3

"""
File names: read_fa_sequences.py

This python script deals with FASTA files in which nucleotide sequence
belonging to a sequence header are written on new lines instead of writing
entire sequence on one line.
"""


def get_sequences(file_path):
    """
    :param file_path: FASTA file path.
    :return: A list of sequences from the input FASTA file.
    """
    with open(file_path, "r") as fin:
        lines = fin.readlines()
        # print(lines)
        all_seqs = []
        headers = []
        seq = []
        for i, line in enumerate(lines):
            if i == 0:
                headers.append(line)
                continue
            if line.startswith(">"):
                headers.append(line)
                all_seqs.append("".join(seq))
                seq = []
            else:
                seq.append(line.strip("\n"))
    # To include the last sequences, as there is no header line after last
    # sequence.
    if len(seq) > 0:
        all_seqs.append("".join(seq))

    print(all_seqs)
    print(headers)


# Test
get_sequences("example.fa")
