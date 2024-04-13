#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:28:11 2024

@author: aleynasuaktas
"""

def min_terms_to_exceed_k(k):
    sum_terms = 0
    num_terms = 0
    while sum_terms < k:
        num_terms += 1
        sum_terms += 1 / num_terms
    return num_terms

def main():
    result = {}
    for k in range(3, 21):
        result[k] = min_terms_to_exceed_k(k)
    print("Dictionary of minimal number of terms needed to be added up in the finite harmonic series:")
    print(result)

if __name__ == "__main__":
    main()
