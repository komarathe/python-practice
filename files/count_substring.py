
"""
File Name: count_substring.py

This file contains a function that return number of occurrence of a substring in
a given DNA string.
"""

import argparse


def main():
    """
    Main Logic
    """
    args = get_cli_args()
    file_path = args.file
    substring = args.substring
    seqs = get_sequences(file_path)
    count_substrings(seqs, substring)


def get_cli_args():
    """
    :return: CLI arguments
    """
    parser = argparse.ArgumentParser(description="Extract sequences from "
                                                 "FASTA file")
    parser.add_argument("file", type=str, help="Path to input FASTA file")
    parser.add_argument("substring", type=str, help="DNA substring")
    return parser.parse_args()


def get_sequences(file_path):
    """
    :param file_path: Input FASTA file
    :return: List of all the sequences in the input FASTA file
    """
    with open(file_path, "r") as fin:
        file_line = fin.readlines()

        seqs = []
        for i in range(1, len(file_line), 1):
            seqs.append(file_line[i].strip())
        return seqs


def count_substrings(seqs, substring):
    """
    :param seqs: DNA sequences collected from input FASTA file
    :param substring: DNA substring we are checking no. of occurrences for
    :return: Total number of occurrences of the substring in each sequence
    """
    for i, seq in enumerate(seqs):
        count = seq.count(substring)
        print("Seq {0} contains {1} occurrences of {2}".format(str(i+1),
                                                               str(count),
                                                               substring))


if __name__ == "__main__":
    main()
