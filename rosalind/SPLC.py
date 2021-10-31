#!/usr/bin/env python3

"""
File name: SPLC.py
Title: RNA Splicing
Refer: http://rosalind.info/problems/splc/

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)
"""

import argparse


def main():
    args = get_cli_args()
    file_path = args.fasta_file
    all_seqs = get_sequences(file_path)
    main_seq = rna_splicing(all_seqs)
    translate(main_seq)


def get_cli_args():
    parser = argparse.ArgumentParser(description="Process FASTA file")
    parser.add_argument("fasta_file", help="Provide path to FASTA file")
    return parser.parse_args()


def get_sequences(file_path):
    fin = open(file_path, "r")
    lines = fin.readlines()
    # Collect headers
    headers = []
    # Collect all sequences
    all_seqs = []
    # To collect whole sequence
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
    fin.close()

    return all_seqs


def rna_splicing(all_seqs):
    main_seq = all_seqs[0]
    introns = all_seqs[1:len(all_seqs)+1]

    for intron in introns:
        main_seq = main_seq.replace(intron, "")

    return main_seq


def translate(main_seq):
    gen_code = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    protein = ""
    for i in range(0, len(main_seq), 3):
        protein = protein + gen_code[main_seq[i:i+3]]
    print(protein.replace("_", ""))


if __name__ == "__main__":
    main()
