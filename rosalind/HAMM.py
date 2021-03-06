#!/usr/bin/env python3

"""
File name: HAMM.py
Refer: http://rosalind.info/problems/hamm/
Counting Point Mutations

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

seq1 = "CTGTACCGTGCGCTTCGGGGACCCGATAAGGTCTCCAACTCTTTGCCAGACAATACCGGGACCACGGT" \
       "GCAAGTCTTGCCGGATTAACAATTGACACGAAGAAACCCTGTGTGGGCCACACTCAGCGGGTATGAGC" \
       "CTTAACTGGAATAAGTTGTCTTAGTAACTGCAGCACCGAGGGTGTAGATCTATTTTCTAAGTGAACAT" \
       "CCAGGCCGATCGTTCACAGCGCGTGACCTGCTGCCCATACGCAGAAGTATGGACAACCATGTGACTAT" \
       "CAGGCCCACGTGAGCGCCAAATTACGGGGCCGTCATCTAGCGTCTTATCCGTAAAGGTAGTGCGACAG" \
       "TGAACGTAATCGATTTGATGGTCTAGACTTGATATATAAATAAGTGACAGACCTAACCACGTGCTGCA" \
       "ATAAGTTCGTAGCCACGTGAACGCACAATACCTGGGCCTGGGTTTTGTGTCAACGTGGGGTATAGCAC" \
       "GCAGGGTAGCTGACTTGTTGCGCTAAGTGATATTAACGAGTGGACTTGAAACCCCGTCTTGGACGTTA" \
       "AAGAGATATGATCGTAACAACCGATAGTATGTCAATTATCGTGCTATTTCTGATTCTAAGGGCGTGCA" \
       "GTAGGGCTGGTACTATCCCGACTCGGAGTTTTGTGCAGGCTCAGTGCCGCCGCTGTGATTCATAGCAG" \
       "ACGGTTCTCACGGCGTTCAAAGCCCCTCCCGCCTGTGCAGTTACCCCGAGACGCTTGATATGGCTGCG" \
       "ATGTAGTTTGTCTTATTCCACCCTGACCCTGCAACGCCCGTTCTCTAGCATCCAAACGTCAAAGTCCT" \
       "GGGGCCTCTTATTTCTGATTTCCCAGAGTGCGGTGAACGCATGCGCGAGGCGTCATCTCGATTGGTTG" \
       "GACGGAAGTCGGACCGCCTGGGTGTTACTCTTTCTTCTAATGCTGCAAAGGTAGTAAGGTCTCAGAAC" \
       "GCATTAGTATAGATTCCCTAACCATAGAGAA"

seq2 = "CCGAAGCGTTAGCCCTAGGGTCCCGACAAAATCCCCATGTATCCGCTGGTCTGTGTCTACACCTCTGC" \
       "CCTAGTCCTTAACCAATCAACTCAAGCCAGTAGTGCCCCACTGTCTACCAAGCAATGCGACCCTTTTG" \
       "CCGTAGTGCAGCAACATGTCTCAACCACTTCGGCCCGGAGGGTTATCATATCTATGCTCAGAGAAGCT" \
       "CATTACCATGGGAACACGCTGCTCGATCCGGGCGTAAAACGAAGAATCATCGAAACCGAGCAGAGTAT" \
       "CATAGCCACATGGGGGCCGGACATCAGCGCCGCAATTTAGCACATTACCCTCAAAGGGAGTACTCATT" \
       "ATGCCATGACGAGATTGATGGAAGGCAGTTGACCGGGCGTGAAGTCTCTGAACTAACCAGTCCCAGAA" \
       "ATGCCGTCCTAGGCACGCGCACGCACCACGTCTGTACCGCACTTTTCTGGCAAATTGGACTCGTGCAC" \
       "CCTCAGATACAGGAAGTCCTAGCCAGGGATAATACACCAAACGACTGTACAACCTATCGAATTTGATT" \
       "AAGAGATACGAGCGCATCTACATAAACTAGAACCACTTTAGTGCTGTTTGCGACCGAGAGGAAGTGCA" \
       "GACTTGGTAGAATTATTGCGCGATGGGCCTCAAAGCTCATCCTGTATCGGTTCCGGGCTGCGAAGGTA" \
       "AAGATTTTCGGGTCTTACACAGCACGAAGTAGTTCTGTCCTAACCCTCAACCCTATTATAAGGATCCG" \
       "TCCTTGAGTCATCCAATTCCAGTTTGCCATGCCATGCCCACTTACATGCGTGCCGAGAAGACAAAAGT" \
       "GGTCAGAGTCGTTTCAATTTACCTTCTGTGATGGAATCTCATGGGCTACCTCGCCCGGCGTATGGATG" \
       "AACCCCAGCCCGACACGCATAAAGTTTCTGTGCCATGCAATACACCCCAAAGCATATGGTCCCGTCCC" \
       "GGATTGATGAATGCGACCTGCCCATCATAAG"

def cal_hamming_dict(seq1, seq2):
    hamm_count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamm_count = hamm_count + 1
    print(hamm_count)

# Test
cal_hamming_dict(seq1, seq2)
