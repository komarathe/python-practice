#!/usr/bin/env python3

"""
File name: MRNA.py
Refer: http://rosalind.info/problems/mrna/
Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein
could have been translated, modulo 1,000,000
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
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}


def main():
    """
    Main logic
    """
    args = get_cli_args()
    aa_seq = args.protein_sequence
    get_possible_aa(aa_seq)


def get_cli_args():
    """
    :return: CLI argument
    """
    parser = argparse.ArgumentParser(description="Process protein sequence")
    parser.add_argument("protein_sequence", help="Provide protein sequence")
    return parser.parse_args()


def get_codons(gen_code_dict):
    """
    :param gen_code_dict: Genetic code dictionary
    :return: Dictionary of amino acid counts for each codon
    """
    aa_dict = {}
    for item in gen_code_dict:
        if gen_code_dict[item] not in aa_dict:
            aa_dict[gen_code_dict[item]] = 1
        else:
            aa_dict[gen_code_dict[item]] += 1
    return aa_dict


def get_possible_aa(aa_seq):
    """
    :param aa_seq: get_codons() output, dictionary of amino acid counts for
    each codon
    """
    codon_count = get_codons(gen_code)
    result = codon_count["_"]
    for aa in aa_seq:
        result = (result * codon_count[aa]) % 1000000
    print(result)


if __name__ == "__main__":
    main()
