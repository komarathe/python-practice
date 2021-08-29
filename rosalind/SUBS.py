#!/usr/bin/env python3

"""
File name: SUBS.py
Refer: http://rosalind.info/problems/subs/
Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""

def find_motif(main_str, sub_str):
    sub_len = len(sub_str)
    motif_positions = []
    for i in range(len(main_str)):
        if main_str[i:(i+sub_len)] == sub_str:
            motif_positions.append(str(i + 1))
    print(" ".join(motif_positions))


# Test
find_motif("GATATATGCATATACTT", "ATAT")
