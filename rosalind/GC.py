#!/usr/bin/env python3

"""
File name: GC.py
Refer: http://rosalind.info/problems/gc/
Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on
absolute error below.
"""

import argparse


def main():
    """
    Main Logic
    :return: Sequence ID with highest GC percent
    """
    args = get_cli_args()
    file_path = args.file
    file_handle = create_file_handle(file_path)
    create_gc_dict(file_handle)
    file_handle.close()


def get_cli_args():
    """
    :return: CLI argument parser
    """
    parser = argparse.ArgumentParser(description="Provide Rosalind FASTA file")
    parser.add_argument("file", help="Input file path")
    return parser.parse_args()


def create_file_handle(file_path):
    """
    :param file_path: Input file path
    :return: File handle
    """
    fin = open(file_path, "r")
    return fin


def cal_gc_percent(line):
    """
    :param line: DNA string
    :return: GC percent
    """
    gc_counter = 0
    for i in range(len(line)):
        if (line[i] == "G") or (line[i] == "C"):
            gc_counter = gc_counter + 1
    return (gc_counter / len(line)) * 100


def create_gc_dict(file_handle):
    """
    :param file_handle: File handle of the input FASTA file.
    :return: Sequence ID of a DNA sequence containing highest GC content.
    """
    id_list = []
    gc_list = []
    for line in file_handle:
        if line.startswith(">"):
            id_list.append(line)
        else:
            gc_list.append(cal_gc_percent(line))
    id_gc_dict = dict(zip(id_list, gc_list))
    # Get the key with maximum value
    max_key = max(id_gc_dict, key=id_gc_dict.get)
    print(max_key + "\r" + str(round(id_gc_dict[max_key], 6)))


if __name__ == "__main__":
    main()
