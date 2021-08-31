#!/usr/bin/env python3

"""
File name: PRTM.py
Title : Calculating Protein Mass
Refer: http://rosalind.info/problems/prtm/
The standard weight assigned to each member of the 20-symbol amino acid
alphabet is the monoisotopic mass of the corresponding amino acid.
Given: A protein string P of length at most 1000 aa.
Return: The total weight of P.
"""

import argparse

aa_weight_dict = {"A": 71.03711, "C": 103.00919, "D": 115.02694,
                  "E": 129.04259, "F": 147.06841, "G": 57.02146,
                  "H": 137.05891, "I": 113.08406, "K": 128.09496,
                  "L": 113.08406, "M": 131.04049, "N": 114.04293,
                  "P": 97.05276, "Q": 128.05858, "R": 156.10111,
                  "S": 87.03203, "T": 101.04768, "V": 99.06841,
                  "W": 186.07931, "Y": 163.06333}

def main():
    args = get_cli_args()
    protein_seq = args.protein_seq
    calc_prot_weight(protein_seq)


def get_cli_args():
    parser = argparse.ArgumentParser(description="Calculate total weight of "
                                                 "protein sequence")
    parser.add_argument("protein_seq", help="Provide protein string")
    return parser.parse_args()


def calc_prot_weight(protein_seq):
    wt = 0.0
    for aa in protein_seq:
        wt = wt + aa_weight_dict[aa]
    print(round(wt, 3))


if __name__ == "__main__":
    main()
