#!/usr/bin/env python3

"""
File name: REVC.py

Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 bp

Return: The reverse complement sc of s
"""

import argparse


def main():
    """
    Main logic
    """
    args = get_cli_args()
    file_path = args.file

    dna = create_file_handle(file_path)
    complement_dna(dna)

    dna.close()


def get_cli_args():
    parser = argparse.ArgumentParser(description="Provide Rosalind data file")
    parser.add_argument("file", help="Input file path")
    return parser.parse_args()


def create_file_handle(file_path):
    """
    :param file_path:
    :return:
    """
    fin = open(file_path, "r")
    return fin


def complement_dna(dna):
    """
    :param dna: File handle of the input file containing DNA string
    :return: Reverse complement of the DNA string
    """
    dna_string = dna.readline()
    reversed_dna = dna_string[::-1]
    a = reversed_dna.replace("A", "t")
    t = a.replace("T", "a")
    c = t.replace("C", "g")
    g = c.replace("G", "c")
    rev_complement = g.upper()
    print(rev_complement)


if __name__ == "__main__":
    main()
