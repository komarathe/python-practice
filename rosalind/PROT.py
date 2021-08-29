#!/usr/bin/env python3

"""
File names: PROT.py
Refer: http://rosalind.info/problems/prot/
Translating RNA into Protein

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""

import argparse

gen_code = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'', 'UAG':'',
    'UGC':'C', 'UGU':'C', 'UGA':'', 'UGG':'W'}


def main():
    """
    Main Logic
    """
    args = get_cli_args()
    file_path = args.file
    rna = get_file_handle(file_path)
    get_protein_string(rna)


def get_cli_args():
    """
    :return: CLI arguments
    """
    parser = argparse.ArgumentParser(description="Provide Rosalind dataset "
                                                 "file")
    parser.add_argument("file", help="Input file path")
    return parser.parse_args()


def get_file_handle(file_path):
    with open(file_path, "r") as fin:
        rna = fin.read()
    return rna


def get_protein_string(rna):
    rna = rna.replace("\n", "")
    rna = rna.replace("\r", "")

    protein = ""
    if len(rna) % 3 == 0:
        for i in range(0, len(rna), 3):
            codon = rna[i:i + 3]
            protein += gen_code[codon]
    print(protein)


if __name__ == "__main__":
    main()

