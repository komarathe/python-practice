#!/usr/bin/env python3

"""
File name: LCSM.py
Refer: http://rosalind.info/problems/lcsm/
Finding a Shared Motif

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each
in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)
"""

import argparse

# Steps:
# 1. parse the FASTA file
# 2. collect all the sequences in a list
# 3. Find the smallest sequence
# 4. Create all possible substrings from the smallest sequence
# 5. Check for each substring if it is present in all sequences
# 6. Collect common substrings
# 7. Find the longest common substring present among all the sequences


def main():
    """
    Main logic
    """
    args = get_cli_args()
    file_path = args.file
    all_seqs = read_sequences(file_path)
    smallest_seq = get_smallest_seq(all_seqs)
    substrings = create_substrings(smallest_seq)
    final_answer(substrings, all_seqs)


def get_cli_args():
    """
    :return: CLI arguments
    """
    parser = argparse.ArgumentParser(description="Extract sequences from "
                                                 "FASTA file")
    parser.add_argument("file", type=str, help="path to input FASTA file")
    return parser.parse_args()


def read_sequences(file_path):
    """
    :param file_path: Input FASTA file path
    :return: List of all sequences
    """
    with open(file_path, "r") as fin:
        lines = fin.readlines()
        # print(lines)
        all_seqs = []
        seq = []
        for i, line in enumerate(lines):
            if i == 0:
                continue
            if line.startswith(">"):
                all_seqs.append("".join(seq))
                seq = []
            else:
                seq.append(line.strip("\n"))
    # To include the last sequences, as there is no header line after last
    # sequence.
    if len(seq) > 0:
        all_seqs.append("".join(seq))

    return all_seqs


def get_smallest_seq(all_seqs):
    """
    :param all_seqs: List of all sequences
    :return: Smallest sequence
    """
    len_seq_dict = {}
    for seq in all_seqs:
        # If there are more sequences having same lengths, value of those
        # keys will be overwritten by latest sequence.
        len_seq_dict[len(seq)] = seq
    sorted_dict = sorted(len_seq_dict)
    return len_seq_dict[sorted_dict[0]]


def create_substrings(smallest_seq):
    """
    :param smallest_seq: Smallest sequence
    :return: All possible substrings of the smallest sequence
    """
    substrings = []
    for i in range(0, len(smallest_seq)+1):
        for j in range(i, len(smallest_seq)+1):
            if i == j:
                continue
            substrings.append(smallest_seq[i:j])
    return substrings


def final_answer(substrings, all_seqs):
    """
    :param substrings: List of all substrings of the smallest sequence
    :param all_seqs: List of all sequences
    :return: Longest common substring
    """
    common_substrings = []
    for item in substrings:
        counter = 0
        for seq in all_seqs:
            if item in seq:
                counter = counter + 1
        if counter == len(all_seqs):
            common_substrings.append(item)
    # Print the longest string
    print(max(common_substrings, key=len))


if __name__ == "__main__":
    main()
