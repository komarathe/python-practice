#!/usr/bin/env python3

"""
File name: RNA.py
Transcribing DNA into RNA

Refer: http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

import argparse

def main():
    """
    Main logic
    """
    args = get_cli_args()
    file_path = args.file
    dna = create_file_handle(file_path)
    transcribe(dna)
    dna.close()



def create_file_handle(file_path):
    """
    :param file_path: Path to the input file
    :return: File handle
    """
    fin = open(file_path, "r")
    return fin


def transcribe(dna):
    """
    :param dna: File handle
    """
    dna_string = dna.readline()
    rna_string = dna_string.replace("T", "U")
    print(rna_string)


def get_cli_args():
    """
    :return: CLI argument parser
    """
    parser = argparse.ArgumentParser(description="Provide Rosalind dataset file")
    parser.add_argument("file", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    main()
