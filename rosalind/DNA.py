#!/usr/bin/env python3
"""
File name: DNA.py
Counting DNA nucleotides.

Refer: http://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number
 of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

import argparse

def main():
    """
    Main logic
    """
    args = get_cli_args()
    file_path = args.file

    dna = create_file_handle(file_path)
    count_nucleotides(dna)
    dna.close()


def get_cli_args():
    """
    :return: CLI argument parser
    """
    parser = argparse.ArgumentParser(description="Provide Rosalind dataset "
                                                 "file")
    parser.add_argument("file", help="Input file path")
    return parser.parse_args()


def create_file_handle(file_path):
    """
    :param file_path: Path to the input file
    :return: File handle
    """
    fin = open(file_path, "r")
    return fin

def count_nucleotides(dna):
    """
    :param dna: input file handle
    """
    dna_string = dna.readline()
    a = dna_string.count("A")
    c = dna_string.count("C")
    g = dna_string.count("G")
    t = dna_string.count("T")
    print(a, c, g, t)

if __name__ == "__main__":
    main()